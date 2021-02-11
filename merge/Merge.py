"""
Merge geospatial building footprint data from multiple sources, following
the hierarchy of ODB > OSM > MS when features overlap.

Usage Example: python Merge.py ab ../data/odb/ab/ODB_Alberta/odb_alberta.shp ../data/osm/ab/gis_osm_buildings_a_free_1.shp ../data/ms/ab/Alberta.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

Data sources:
    - Open Database of Buildings (ODB), provided by Statistics Canada.
    - Open Street Map buildings (OSM), downloaded from geofabrik.de.
    - Microsoft Canadian Building Footprints (MS)
    - Census Subdivisions (CSD), provided by Statistics Canada.
"""
import time
import os.path
import sys
import geopandas as gpd
from geopandas.tools import sjoin



def copy_csd_data(gdf, csd):
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
    gdf['CSDNAME'] = gdf_centroids_csd_join['CSDNAME']
    gdf['Shape_Area'] = gdf_centroids_csd_join.geometry.area
    gdf['Shape_Leng'] = gdf_centroids_csd_join.geometry.length

    # Update joined centroids dataframe to epsg:4326 to provide DD values
    gdf_centroids_csd_join = gdf_centroids_csd_join.to_crs('epsg:4326')
    gdf['Longitude'] = gdf_centroids_csd_join.geometry.x
    gdf['Latitude'] = gdf_centroids_csd_join.geometry.y

    return gdf



def combine_building_footprints(odb_gdf, osm_gdf, ms_gdf):
    """
    Combines the three building footprint data sources

    Attributes
    ----------
    odb_gdf - geodataframe
        Geodataframe containing the odb building footprints
    osm_gdf - geodataframe
        Geodataframe containing the osm building footprints
    ms_gdf - geodataframe
        Geodataframe containing the ms building footprints

    Returns
    -------
    final - geodataframe
        Geodataframe with the odb, osm, and ms geodataframes appended.
    """

    # Combine OSM and MS geodatframes
    temp = osm_gdf.append(ms_gdf)

    # Combine ODB with previously combined osm/ms geodataframe
    if odb_gdf is not None:
        final = odb_gdf.append(temp)
    else:
        final = temp

    return final


def main(region, odb_file, osm_file, ms_file, csd_file):
    """
    Main entry point of the merging script

    Attributes
    ----------
    region: str
        A two character province or territory code (e.g. NU, PE, NB, etc).
    odb_file: str
        File location for Open Database of Buildings building footprints.
        If no data is available, value is set to None
    osm_file: str
        File location for Open Street Map building footprints.
    ms_file: str
        File location for Microsft building footprints.
    csd_file: str
        File location for census subdivision file.
    """

    start_time = time.time()

    # ID map based on values contained in the PRUID field in lcsd dataset
    prov_terr_id_map = {
        'AB': '48',
        'BC': '59',
        'MB': '46',
        'NB': '13',
        'NL': '10',
        'NS': '12',
        'NT': '61',
        'NU': '62',
        'ON': '35',
        'PE': '11',
        'QC': '24',
        'SK': '47',
        'YT': '60'
    }

    pr_terr_abrv = None

    # Check if region is valid
    if region.upper() in list(prov_terr_id_map.keys()):
        pr_terr_abrv = region.upper()
        pr_terr_id = prov_terr_id_map[pr_terr_abrv]

    # If the arguments are valid proceed with sampling of data
    if pr_terr_abrv:

        # -------------------------------------------------
        # Load each dataset
        # -------------------------------------------------
        # Read ODB dataset
        if odb_file:
            print("Reading ODB Dataset ...")
            odb = gpd.read_file(odb_file)
            odb_unique = odb

        # Read OSM dataset
        print("Reading OSM Dataset ...")
        osm = gpd.read_file(osm_file)

        # Read Microsoft dataset
        print("Reading Microsoft Dataset ...")
        ms = gpd.read_file(ms_file)

        # Read CSD dataset
        print("Reading Census Subdivision Dataset ...")
        csd = gpd.read_file(csd_file)

        # Query CSD features for the province/territory being processed
        print("Querying Census Subdivision Dataset to Only include features in selected {}".format(pr_terr_abrv))
        csd = csd[csd['PRUID'] == pr_terr_id]

        # Drop all but CSDUID, CSDNAME, and geometry fields from csd
        csd = csd[['CSDUID', 'CSDNAME', 'geometry']]

        # Update CRS of MS and OSM data to match ODB EPSG:3347 CRS
        print("Updating OSM and MS Coordinate Reference Systems")
        osm=osm.to_crs('epsg:3347')
        ms=ms.to_crs('epsg:3347')

        # -------------------------------------------------
        # Find Intersections between different datasets
        # Hierarchy followed; ODB > OSM > MS
        # -------------------------------------------------
        if odb_file:
            print("Find intersection between ODB and OSM")
            odb_osm_intersection = sjoin(osm, odb, how="left", op="intersects")

            print("Find intersection between ODB and MS")
            odb_ms_intersection = sjoin(ms, odb, how="left", op="intersects")

            # Exclude ODB Footprints from OSM data-sets if they already exists
            print("Get unique OSM features which don't exist as ODB building footprints")
            osm_unique = odb_osm_intersection[odb_osm_intersection.CSDNAME.isnull()]

            # Remove unneeded spatial join columns
            osm_unique = osm_unique[osm.columns]

            # Exclude ODB Footprints from MS data-sets if they already exists
            print("Get unique MS features which don't exist as ODB building footprints")
            ms_unique = odb_ms_intersection[odb_ms_intersection.CSDNAME.isnull()]

            # Remove unneeded spatial join columns
            ms_unique = ms_unique[ms.columns]

        else:
            osm_unique = osm
            ms_unique = ms

        print("Find an intersection between unique OSM and MS features")
        osm_ms_intersection = sjoin(ms_unique, osm_unique, how="left", op="intersects")

        # Exclude OSM building footprints from MS data-set if they already exists
        print("Get MS features which exist as OSM building footprints")
        ms_unique = osm_ms_intersection[osm_ms_intersection.osm_id.isnull()]

        # Remove unneeded spatial join columns
        ms_unique = ms_unique[ms.columns]

        if odb_file:
            odb_unique = odb_unique.to_crs('epsg:4326')

            # Fixes issue with one of the provinces (AB) having an inconsistent column name
            if 'data_prov' in odb_unique.columns:
                odb_unique['Data_prov'] = odb_unique['data_prov']
                del odb_unique['data_prov']

        # -------------------------------------------------
        print("Copy CSD data to building footprint features")
        osm_unique = copy_csd_data(osm_unique, csd)
        osm_unique['Data_prov'] = 'OSM'

        ms_unique = copy_csd_data(ms_unique, csd)
        ms_unique['Data_prov'] = 'Microsoft'
        # -------------------------------------------------
        print('Appending ODB, OSM, MS together')
        if odb_file:
            odb_osm_ms_combined = combine_building_footprints(odb_unique, osm_unique, ms_unique)
        else:
            odb_osm_ms_combined = combine_building_footprints(None, osm_unique, ms_unique)

        # -------------------------------------------------
        print("Delete old geodataframes to free up memory")
        if odb_file:
            del odb
            del odb_unique

        del osm
        del ms
        del osm_unique
        del ms_unique

        # -------------------------------------------------
        print('Generate a unique id for each building footprint feature')
        n = len(odb_osm_ms_combined.geometry)
        build_id = []
        for i in range(1, n + 1):
            # create a build id by combining the prov/terr id and a unique 7 digit number
            build_id.append(pr_terr_id +f'{i:07d}')

        odb_osm_ms_combined['Build_ID'] = build_id

        # -------------------------------------------------
        print('Exporting GeoJSON')
        odb_osm_ms_combined.to_file('merge/output/odb_osm_ms_merged_building_footprints_'+pr_terr_abrv+'.geojson', driver='GeoJSON')

        end_time = time.time()

        print("Time to complete processing: {} mins".format((end_time-start_time)/60))


def valid_input_files(odb_file, osm_file, ms_file, csd_file):
    """
    Checks if the input files provides as arguments are valid

    Attributes
    ----------
    odb_file: str
        path to the province/territory odb file
    osm_file: str
        path to the province/territory osm file
    ms_file: str
        path to the province/territory ms file
    csd_file: str
        path to the census subdivison file

    Returns
    -------
    valid: bool
        If all of the passed arguments are valid, return True, otherwise return False
    """
    valid = False

    if os.path.exists(ms_file):
        if os.path.exists(osm_file):
            if os.path.exists(csd_file):
                if odb_file is None:
                    valid = True
                elif os.path.exists(odb_file):
                    valid = True

    return valid


if __name__ == "__main__":
    if len(sys.argv) == 6:
        args = sys.argv
        if valid_input_files(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]):
            main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

    elif len(sys.argv) == 5:
        # if only 4 arguments are provided, it's assumed no odb available
        args = sys.argv
        if valid_input_files(None, sys.argv[2], sys.argv[3], sys.argv[4]):
            main(sys.argv[1], None, sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        raise SyntaxError("Invalid number of arguments.")

