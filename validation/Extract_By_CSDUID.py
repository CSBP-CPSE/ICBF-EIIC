"""
Extract building footprints based on CSDUID 

Usage Example: python Extract_By_CSDUID.py 3506008 ../data/osm/on/gis_osm_buildings_a_free_1.shp ../data/lcsd000b16a_e/lcsd000b16a_e.shp
"""
import os.path
import sys
import geopandas as gpd
from geopandas.tools import sjoin


def copy_csduid(gdf, csd):
    """
    Copy csd field data/calculate geometry data to geodataframe

    Attributes
    ----------
    gdf: geodataframe
        Geodataframe containing the building footprint data
    csd: geodataframe
        Geodataframe containing the Census Subdivision data

    Returns
    -------
    gdf: geodataframe
        An updated geodataframe with new fields containing csd and geometry data.
    """
    gdf_centroids = gpd.GeoDataFrame(gdf.centroid, geometry = gdf.centroid, crs = gdf.crs)

    gdf_centroids_csd_join = sjoin(gdf_centroids, csd, how = 'left', op = 'within')

    gdf = gdf.to_crs('epsg:4326')

    gdf['CSDUID'] = gdf_centroids_csd_join['CSDUID']

    return gdf


def main(csduid, bf_file, csd_file):
    """
    Main entry point for application

    Attributes
    ----------
    csduid: str
        A CSDUID (e.g. 3506008).
    bf_file: str
        File location for building footprints.
    csd_file: str
        File location for census subdivision file.
    """

    # If the arguments are valid proceed with sampling of data
    if csduid and os.path.exists(bf_file) and os.path.exists(csd_file):

        # -------------------------------------------------
        # Load each dataset
        # -------------------------------------------------
        # Read Building Footprints dataset
        print("Reading Building Footprints Dataset ...")
        bf = gpd.read_file(bf_file)

        # Read CSD dataset
        print("Reading Census Subdivision Dataset ...")
        csd = gpd.read_file(csd_file)

        # Update building footprint crs to match csd crs
        bf = bf.to_crs(csd.crs)

        # Copy CSDUID to dataset
        bfcsd = copy_csduid(bf, csd)
    
        bfcsd = bfcsd[bfcsd['CSDUID'] == csduid]

        # Export all building features for each randomnly selected csd
        print('Exporting CSD ' + csduid + ' building footprints')
        bfcsd.to_file(csduid+'_output.geojson', driver = 'GeoJSON')


if __name__ == "__main__":
    if len(sys.argv) == 4:
        args = sys.argv
        main(str(sys.argv[1]), sys.argv[2], sys.argv[3])
    else:
        raise SyntaxError("Invalid number of arguments.")
