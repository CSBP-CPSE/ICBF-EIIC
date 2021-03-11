"""
Simple script for splitting up merged provincial building footprint geojson datasets
by source (OpenStreetMap, Microsoft, or Open Database of Buildings).

* OpenStreetMap (OSM) data is identified as having a Data_prov column value == 'OSM'
* Microsoft (MS) data is identified as having a Data_prov column value == 'Microsoft'
* Open Database of Buildings (ODB) is identified as having a Data_prov column value not equal to either 'OSM' or
'Microsoft'. i.e. all other data is provided by ODB source.

Syntax: python split_geojson_by_source.py <directory containing odb_osm_ms_odb_osm_ms_merged_building_footprints_[Prov/Terr code].geojson> files
Usage Example: python split_geojson_by_source.py data/
"""
import sys
import os
import geopandas as gpd
from tqdm import tqdm


def main(inputs_dir):
    """
    Entry point for merge and split processing script

    Attributes:
    ------------
    :param inputs_dir {string} - Path to the directory containing input data
    """

    # Create output directory if it doesn't exist
    if not os.path.exists('output/'):
        os.mkdir('output')

    # Iterate over geojson files in data directory, splitting merged datasets by three data providers
    for filename in tqdm(os.listdir(inputs_dir)):
        if filename.endswith(".geojson"):
            print("Processing: {}".format(os.path.join(inputs_dir, filename)))
            fname = filename[18:]
            geodf = gpd.read_file(inputs_dir + filename)

            # Get all OSM Data and output it to a new file
            osm_geodf = geodf[geodf['Data_prov'] == 'OSM']
            if not osm_geodf.empty:
                osm_geodf.to_file('output/osm_' + fname, driver='GeoJSON')
                # Remove OSM records from geodf
                geodf = geodf[geodf['Data_prov'] != 'OSM']

            # Get All MS Data and output it to a new file
            ms_geodf = geodf[geodf['Data_prov'] == 'Microsoft']
            if not ms_geodf.empty:
                ms_geodf.to_file('output/ms_' + fname, driver='GeoJSON')
                # Remove Microsoft records from geodf
                geodf = geodf[geodf['Data_prov'] != 'Microsoft']

            # Output ODB Data
            if not geodf.empty:
                geodf.to_file('output/odb_' + fname, driver='GeoJSON')

            # Delete old geo-dataframes
            del geodf
            del ms_geodf
            del osm_geodf


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        raise SyntaxError("Invalid number of arguments")
