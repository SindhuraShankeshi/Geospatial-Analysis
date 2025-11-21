# Interactive Geospatial Analysis with Python & Folium

A compact, hands-on project that demonstrates interactive geospatial visualization using Python and Folium through two case studies: San Francisco crime clustering and a world choropleth showing migration to Canada.

## Table of contents
- [Overview](#overview)
- [Features](#features)
- [Repository structure](#repository-structure)
- [Data sources](#data-sources)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples & outputs](#examples--outputs)
- [Development & contribution](#development--contribution)
- [License & contact](#license--contact)

## Overview
This repository contains code and assets to:
- Visualize high-density point data using MarkerCluster (San Francisco crime incidents).
- Produce choropleth maps from tabular data bound to GeoJSON geometries (migration to Canada).
The focus is on reproducible, easy-to-run notebooks/scripts that produce interactive HTML maps viewable in any browser.

## Features
- Interactive Leaflet maps via Folium
- Marker clustering for dense point datasets
- Choropleth generation from Pandas DataFrames and GeoJSON
- Pop-ups and simple styling for improved exploration
- Minimal, dependency-light Python code so maps can be generated locally

## Repository structure
(Adjust these paths if your repository structure differs.)
- notebooks/
  - sf_crime_analysis.ipynb         # Notebook to generate clustered SF crime map
  - migration_choropleth.ipynb      # Notebook to generate world choropleth for Canada migration
- data/
  - sf_crime_2016.csv               # (example) SF PD dataset (2016)
  - migration_to_canada_1980_2013.csv
  - world_countries.geojson
- images/
  - sf_crime_map.png
  - world_choropleth.png
- scripts/
  - generate_maps.py                # Optional script version to create and save maps
- README.md

## Data sources
- San Francisco Police Department (SF Open Data) — crime incidents (2016). Please verify license/usage and remove any sensitive fields before publishing.
- United Nations / public migration data (1980–2013) — aggregated to country-to-country flows.
- World GeoJSON (public domain / Natural Earth-derived files).

Always keep raw data out of version control if it contains sensitive or very large files; include a small sample or instructions to download the full dataset.

## Requirements
- Python 3.8+ recommended
- Key Python libraries:
  - pandas
  - folium
  - numpy
  - jupyter (for running notebooks, optional)

A minimal requirements.txt would look like:
```bash
pandas
folium
numpy
jupyter
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/SindhuraShankeshi/Geospatial-Analysis.git
cd Geospatial-Analysis
```

2. Create a virtual environment (recommended) and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows (PowerShell)
pip install -r requirements.txt
```
If you don't have a requirements.txt, you can install the main libs directly:
```bash
pip install pandas folium numpy jupyter
```

## Usage
- Notebooks:
  - Start Jupyter:
    ```bash
    jupyter notebook
    ```
  - Open the notebooks in `notebooks/` (e.g., `sf_crime_analysis.ipynb`) and run the cells. The notebook will generate interactive maps and usually save them as HTML files.

- Script:
  - If a script `scripts/generate_maps.py` exists, run:
    ```bash
    python scripts/generate_maps.py
    ```
  - Script arguments (if implemented) might include input file paths and output names.

- Viewing generated maps:
  - The notebooks/scripts typically call `map.save("sf_crime_map.html")` or similar. Open the saved HTML in your browser.

## Examples & outputs
- images/sf_crime_map.png — a screenshot of a clustered SF crime map (place a screenshot here to document results).
- images/world_choropleth.png — a screenshot of the choropleth map showing migration to Canada.

Tip: When sharing maps, include the generated .html (or a link) alongside the screenshots so others can interact with the visualization.

## Development & contribution
- If you want help adding:
  - a requirements.txt (I can generate one from your environment),
  - ready-to-run scripts that mirror the notebooks,
  - pre-built sample datasets (small subsets),
  I can prepare those and open a PR-style patch you can review.

- Contributions are welcome — open an issue to discuss feature requests or bug reports, and submit PRs for changes.

## License & contact
- Add your preferred license (e.g., MIT, Apache-2.0). If none is included yet, I recommend adding a LICENSE file.
- Contact: SindhuraShankeshi (GitHub) — update this line with preferred email or profile link.

Acknowledgements
- Folium (Leaflet.js) for interactive maps
- Public data providers (SF Open Data, UN / migration datasets)
