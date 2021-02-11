"""
A geospatial script to remove duplicate geometries in a collection of features.
"""
import sys
import geopandas as gpd


def main(input_file):
    """
    Entry point for removing duplicate geometries in a dataset

    Attributes:
    ---------------
    :param input_file {string} - Path to input file
    """

    # Read geospatial features in input file
    input_features = gpd.read_file(input_file)

    # Drop duplicates in input_features
    unique_features = input_features.drop_duplicates()

    # Export unique input_features
    unique_features.to_file('unique_' + input_file, driver='GeoJSON')

    # Print number of duplicate features dropped
    print("{} of {} duplicate features dropped in {}".format(len(input_features.geometry) - len(unique_features.geometry), len(input_features.geometry), input_file))


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        args = sys.argv
        main(sys.argv[1])
    else:
        raise SyntaxError("Invalid number of arguments.")
