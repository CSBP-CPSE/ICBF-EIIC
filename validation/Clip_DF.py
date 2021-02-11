"""
Clip building footprints based on provide clip spatial feature

Usage Example: python Clip_DF.py ../data/osm/on/gis_osm_buildings_a_free_1.shp ../data/study_area/study_area.shp
"""
import os.path
import sys
import geopandas as gpd
from geopandas.tools import sjoin


def main(bf_file, clip_file):
    """
    Main entry point for application

    Attributes
    ----------
    bf_file: str
        File location for building footprints.
    clip_file: str
        File location for clip file.
    """

    # If the arguments are valid proceed with extracting data
    if os.path.exists(bf_file) and os.path.exists(clip_file):

        # Read Building Footprints dataset
        print("Reading Building Footprints Dataset ...")
        bf = gpd.read_file(bf_file)
        bf = bf.to_crs('epsg:3347')

        # Read clip dataset
        print("Reading Census Subdivision Dataset ...")
        clip = gpd.read_file(clip_file)
        clip = clip.to_crs('epsg:3347')

        # Clip building footprints
        bf_clip = gpd.clip(bf, clip)
        
        # Export clipped building features
        print('Exporting clipped building footprints')
        bf_clip.to_file('clip_output.geojson', driver = 'GeoJSON')


if __name__ == "__main__":
    if len(sys.argv) == 3:
        args = sys.argv
        main(str(sys.argv[1]), sys.argv[2])
    else:
        raise SyntaxError("Invalid number of arguments.")
