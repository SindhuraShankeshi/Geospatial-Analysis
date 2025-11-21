# Interactive Geospatial Analysis with Python & Folium

## Overview
This project demonstrates the use of Python's **Folium** library to perform geospatial data analysis and visualization. The project focuses on two distinct case studies: analyzing crime incident density in San Francisco and visualizing global migration trends to Canada using Choropleth maps.

## Key Features
* **Interactive Mapping:** Utilization of Leaflet.js via Folium to create zoomable, interactive maps.
* **Cluster Analysis:** Implementation of `MarkerCluster` to handle high-density data points (SF Crime Data).
* **Choropleth Visualization:** Mapping statistical variables to geometric regions using GeoJSON data.
* **Data Preprocessing:** Using **Pandas** to clean and structure datasets for geospatial rendering.

## Technologies Used
* **Python 3.x**
* **Folium** (Geospatial visualization)
* **Pandas** (Data manipulation)
* **Numpy** (Scientific computing)

## Project Sections

### 1. San Francisco Crime Analysis
Using dataset from the SF Police Department (2016), this section visualizes crime hotspots.
* **Technique:** Visualized 150,000+ incidents reduced to manageable clusters.
* **Feature:** Added pop-ups to individual markers to display crime category (e.g., Larceny, Assault).
* **Visual Style:** Used `CartoDB dark_matter` tiles for high-contrast data visualization.

![SF Crime Map Screenshot](images/sf_crime_map.png)
*(Note: You should take a screenshot of your clustered map and put it in the images folder)*

### 2. Global Migration to Canada (Choropleth)
Using United Nations migration data, this section visualizes the flow of immigrants to Canada from 1980 to 2013.
* **Technique:** Choropleth mapping binding Pandas dataframes to World GeoJSON files.
* **Insight:** The map highlights that the highest immigration numbers during this period originated from China, India, and the Philippines (indicated by darker red hues).

![Choropleth Map Screenshot](images/world_choropleth.png)
*(Note: Take a screenshot of the red world map and put it here)*

## How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pandas folium numpy
