#!/usr/bin/env python3
"""
scripts/generate_maps.py

Simple, runnable script to reproduce the two example maps in this repo:
- San Francisco clustered crime map (HTML)
- World choropleth showing migration to Canada (HTML)

Usage:
    python scripts/generate_maps.py \
        --sf-csv data/sf_crime_2016.csv \
        --migration-csv data/migration_to_canada_1980_2013.csv \
        --world-geojson data/world_countries.geojson \
        --out-dir outputs

Notes:
- The script tries to auto-detect common latitude/longitude column names for the SF dataset.
- The choropleth expects the migration CSV to have either a country ISO code column
  that matches the GeoJSON "id" property (iso_a3/ISO3) or a country name that matches
  the GeoJSON "properties.name". Adjust the keys or pre-process your data when needed.
- This is intentionally lightweight: for more complex transformations, prefer the notebooks.
"""

import os
import argparse
import sys
import json
from pathlib import Path

import pandas as pd
import folium
from folium.plugins import MarkerCluster


def find_lat_lon_columns(df):
    candidates = {
        'lat': ['lat', 'latitude', 'y', 'y_coord', 'ycoord', 'Latitude', 'LAT'],
        'lon': ['lon', 'lng', 'longitude', 'x', 'x_coord', 'xcoord', 'Longitude', 'LON']
    }
    lat_col = next((c for c in candidates['lat'] if c in df.columns), None)
    lon_col = next((c for c in candidates['lon'] if c in df.columns), None)
    return lat_col, lon_col


def generate_sf_cluster_map(sf_csv, out_path, max_points=200000):
    print(f"Loading SF crime data from {sf_csv} ...")
    df = pd.read_csv(sf_csv)

    lat_col, lon_col = find_lat_lon_columns(df)
    if not lat_col or not lon_col:
        raise ValueError(
            "Could not find latitude/longitude columns in the SF CSV. "
            "Expected columns like 'lat','latitude','lng','lon','y','x', etc."
        )

    # Drop rows without coordinates
    df = df.dropna(subset=[lat_col, lon_col])
    # Optionally limit the number of points used for performance
    if len(df) > max_points:
        df = df.sample(n=max_points, random_state=1)

    # Center map on median coordinates
    center_lat = df[lat_col].median()
    center_lon = df[lon_col].median()

    m = folium.Map(location=[center_lat, center_lon], tiles='CartoDB dark_matter', zoom_start=12)
    marker_cluster = MarkerCluster(name="Crime Incidents", disableClusteringAtZoom=16).add_to(m)

    # Pop-up content: try to include a category column if present
    category_col = next((c for c in ['category', 'Category', 'crime_type', 'offense'] if c in df.columns), None)

    for _, row in df.iterrows():
        popup_text = None
        if category_col:
            popup_text = str(row.get(category_col, ''))
        folium.CircleMarker(
            location=[row[lat_col], row[lon_col]],
            radius=4,
            color='#ff7800',
            fill=True,
            fill_opacity=0.7,
            popup=popup_text
        ).add_to(marker_cluster)

    m.save(out_path)
    print(f"Saved SF crime map to {out_path}")


def generate_choropleth(migration_csv, world_geojson, out_path,
                        geojson_id_field=None, migration_country_field=None, migration_value_field=None):
    print(f"Loading migration data from {migration_csv} ...")
    mdf = pd.read_csv(migration_csv)

    # Heuristics for columns
    migration_value_field = migration_value_field or next((c for c in mdf.columns if c.lower() in ('value', 'count', 'immigrants', 'migration', 'num')), None)
    migration_country_field = migration_country_field or next((c for c in mdf.columns if c.lower() in ('country', 'country_name', 'origin', 'iso_a3', 'iso3', 'iso')), None)

    if migration_country_field is None or migration_value_field is None:
        raise ValueError("Could not identify country or value columns in migration CSV. "
                         "Please provide --migration-country-field and --migration-value-field flags.")

    print(f"Using country field '{migration_country_field}' and value field '{migration_value_field}'")

    with open(world_geojson, 'r', encoding='utf-8') as fh:
        gj = json.load(fh)

    # Determine GeoJSON ID field (if features use an 'id' property for matching)
    if geojson_id_field is None:
        # Try common properties
        sample_props = gj['features'][0].get('properties', {})
        geojson_id_field = next((f for f in ('iso_a3', 'ISO_A3', 'iso3', 'id', 'ADM0_A3', 'ISO3') if f in sample_props), None)

    # Prepare mapping for choropleth key_on
    if geojson_id_field:
        key_on = f'feature.properties.{geojson_id_field}'
        print(f"Matching migration rows to GeoJSON by properties.{geojson_id_field}")
    else:
        # Fall back to names
        key_on = 'feature.properties.name'
        print("No ISO-like id found in GeoJSON; falling back to match on feature.properties.name")

    # Prepare DataFrame for folium.Choropleth
    # If migration_country_field contains ISO codes and geojson_id_field exists, match directly.
    choro_df = mdf[[migration_country_field, migration_value_field]].copy()
    choro_df.columns = ['country_key', 'value']

    # Create the map centered at (0,0) and zoomed out
    m = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB positron')

    folium.Choropleth(
        geo_data=gj,
        name='choropleth',
        data=choro_df,
        columns=['country_key', 'value'],
        key_on=key_on,
        fill_color='YlOrRd',
        fill_opacity=0.8,
        line_opacity=0.2,
        legend_name='Migration to Canada (sample period)'
    ).add_to(m)

    folium.LayerControl().add_to(m)
    m.save(out_path)
    print(f"Saved choropleth map to {out_path}")


def parse_args(argv):
    p = argparse.ArgumentParser(description="Generate example Folium maps for the repository.")
    p.add_argument('--sf-csv', required=True, help="Path to SF crime CSV (point dataset).")
    p.add_argument('--migration-csv', required=True, help="Path to migration-to-Canada CSV (country, value).")
    p.add_argument('--world-geojson', required=True, help="Path to world GeoJSON file.")
    p.add_argument('--out-dir', default='outputs', help="Directory to write generated HTML maps.")
    p.add_argument('--sf-out', default='outputs/sf_crime_map.html', help="SF map HTML output path.")
    p.add_argument('--choropleth-out', default='outputs/world_choropleth.html', help="Choropleth HTML output path.")
    p.add_argument('--migration-country-field', default=None, help="Column name in migration CSV for country/ISO.")
    p.add_argument('--migration-value-field', default=None, help="Column name in migration CSV for the numeric value.")
    p.add_argument('--geojson-id-field', default=None, help="GeoJSON property to match migration country keys (e.g., iso_a3).")
    return p.parse_args(argv)


def main(argv):
    args = parse_args(argv)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    sf_out = Path(args.sf_out)
    choropleth_out = Path(args.choropleth_out)

    try:
        generate_sf_cluster_map(args.sf_csv, str(sf_out))
    except Exception as e:
        print("Error generating SF map:", e, file=sys.stderr)

    try:
        generate_choropleth(
            args.migration_csv,
            args.world_geojson,
            str(choropleth_out),
            geojson_id_field=args.geojson_id_field,
            migration_country_field=args.migration_country_field,
            migration_value_field=args.migration_value_field
        )
    except Exception as e:
        print("Error generating choropleth:", e, file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1:])
