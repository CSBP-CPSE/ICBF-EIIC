"""
Geospatial script for combining a collection of input data, and then splitting
the combined data based on field in a specified split feature data-set.

Usage Example: python merge_and_split.py input/ms split/lpr_000b16a_e.shp PRUID
"""
import sys
import os
import geopandas as gpd
import geopandas.tools as gdptools
from tqdm import tqdm

INPUT_CRS = 'epsg:3347'
PRUID_ABRV_MAP = {
    '48': 'AB',
    '59': 'BC',
    '46': 'MB',
    '13': 'NB',
    '10': 'NL',
    '12': 'NS',
    '61': 'NT',
    '62': 'NU',
    '35': 'ON',
    '11': 'PE',
    '24': 'QC',
    '47': 'SK',
    '60': 'YT'
}


def combine_inputs(input_dir):
    """
    Combine a directory of spatial data into a single geodataframe

    Attribute:
    -------------
    :param input_dir {string} - Path to the input directory.

    Returns:
    -------------
    combined_data {GeoDataFrame} - A GeoDataFrame containing the combined input data
    """
    combined_data = None

    print("Combining all input data")
    # Check if the input directory exists:
    if os.path.isdir(input_dir):
        for file in tqdm(os.listdir(input_dir)):
            file_ext = file.split('.')[-1]
            if file_ext == 'shp' or file_ext == 'geojson':
                print("\nReading input file {}".format(file))
                temp = gpd.read_file(input_dir + '/' + file)
                temp = temp.to_crs(INPUT_CRS)

                if combined_data is not None:
                    combined_data = combined_data.append(temp)
                else:
                    combined_data = temp

    return combined_data


def split_data_by_split_field(input_data, split_field):
    """
    Split combined input data by intersecting it with the split features, and breaking up
    the input data based on the specified field in the split data-set.

    Attributes:
    -------------
    :param input_data {GeoDataFrame} - GeoDataFrame containing the combined collection of input data
    :param split_field {string} - Name of field used to split of GeoDataFrame into separate GeoJSON files
    """
    print("Splitting up input data:")
    unique_split_values = input_data[split_field].unique()

    for split_value in tqdm(unique_split_values):
        if isinstance(split_value, str):
            split_data = input_data[input_data[split_field] == split_value]

            # Remove PRUID column if it exists
            if 'PRUID' in split_data.columns:
                del split_data['PRUID']

            # Drop any duplicates in the split dataset
            unique_split_features = split_data.drop_duplicates()

            # Export unique input_features
            unique_split_features.to_file('output/' + PRUID_ABRV_MAP[split_value] + '.geojson', driver='GeoJSON')

            # Print number of duplicate features dropped
            print("{} of {} duplicate features dropped in {}".format(
                len(split_data.geometry) - len(unique_split_features.geometry), len(split_data.geometry), PRUID_ABRV_MAP[split_value]))


def main(inputs_dir, split_data, split_field):
    """
    Entry point for merge and split processing script

    Attributes:
    ------------
    :param inputs_dir {string} - Path to the directory containing input data
    :param split_data {string} - Path to the geospatial file used for splitting the combined input data
    :param split_field {string} - Field name in split data used for dividing up combined input data
    """
    # Combine input files into a single input dataframe
    inputs_df = combine_inputs(inputs_dir)

    # Read geospatial features used for splitting data
    split_features = gpd.read_file(split_data)
    split_features = split_features.to_crs(INPUT_CRS)

    # Create centroids for all input data
    input_centroids = gpd.GeoDataFrame(inputs_df.centroid, geometry=inputs_df.centroid, crs=inputs_df.crs)

    # Intersect split data with input centroids
    intersected_data = gdptools.sjoin(input_centroids, split_features, how='left', op='within')

    # Copy intersected split field value to input dataframe
    inputs_df[split_field] = intersected_data[split_field]

    # Split input data used split data
    split_data_by_split_field(inputs_df, split_field)


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        raise SyntaxError("Invalid number of arguments")
