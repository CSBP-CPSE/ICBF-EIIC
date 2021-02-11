"""
Geospatial script for getting stats on the spatial data.
"""
import csv
import sys
import os
import geopandas as gpd
import geopandas.tools as gdptools
from tqdm import tqdm


def main(data_dir):
    """
    Entry point for stat script

    Attributes:
    ------------
    :param data_dir {string} - Path to the directory containing input data
    """
    with open('building_data_stats.csv', 'w', newline='') as csvfile:
        stats_data = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        stats_data.writerow(['prov_terr', 'total_buildings', 'odb_buildings', 'osm_buildings', 'ms_buildings'])

        if os.path.isdir(data_dir):
            for file in tqdm(os.listdir(data_dir)):
                row = []
                print("\nReading input file {}".format(file))
                gdf = gpd.read_file(data_dir + '/' + file)
                print("File: " + file)
                row.append(file)
                print("Total Features: " + str(len(gdf.geometry)))
                row.append(len(gdf.geometry))
                osm_gdf = gdf[gdf['Data_prov'] == 'OSM']
                ms_gdf = gdf[gdf['Data_prov'] == 'Microsoft']
                print("ODB: " + str(len(gdf.geometry) - len(ms_gdf.geometry) - len(osm_gdf.geometry)))
                row.append(len(gdf.geometry) - len(ms_gdf.geometry) - len(osm_gdf.geometry))
                print("OSM: " + str(len(osm_gdf.geometry)))
                row.append(len(osm_gdf.geometry))
                print("MS: " + str(len(ms_gdf.geometry)))
                row.append(len(ms_gdf.geometry))
                stats_data.writerow(row)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        raise SyntaxError("Invalid number of arguments")
