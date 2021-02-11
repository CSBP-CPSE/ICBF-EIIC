"""
A geospatial script to remove specified fields to drop from spatial data.
"""
import fiona
import sys
from tqdm import tqdm


def remove_fields_from_features(input_features, fields_to_drop):
    """
    Remove specified fields from spatial data

    Attributes:
    --------------------
    :param input_features {string} - File location of the input data
    :param fields_to_drop {string} - List of fields to be dropped from data. e.g. "a,b,c"
    """
    output_file = input_features.name + '_removed_fields.geojson'

    with fiona.open(output_file, 'w', driver='GeoJSON', crs=input_features.crs, schema=input_features.schema) as output:

        # Update input schema by removing dropped fields
        for drop_field in fields_to_drop:
            if 'properties' in output.schema:
                properties = output.schema['properties']
                if drop_field in properties:
                    del properties[drop_field]

            # Update output schema properties with changes
            output.schema['properties'] = properties

        # Update all geometries by removing dropped fields
        for elem in tqdm(input_features, position=0, leave=True):
            # Remove element properties
            updated_elem_props = elem['properties']

            for drop_field in fields_to_drop:
                if drop_field in updated_elem_props:
                    del updated_elem_props[drop_field]

            # Output geometries with reduced coordinate precision
            output.write({
                'geometry': elem['geometry'],
                'properties': updated_elem_props
            })

        print("Finished removing dropped fields from {}".format(input_features.name))


def main(input_file, dropped_fields):
    """
    Entry point for removing fields from input data

    Attributes:
    -------------
    :param input_file {string} - Path to input file
    :param dropped_fields {string} - A list of fields to be dropped from input file (e.g. 'foo,bar,test')
    """
    print("Opening input data...")
    with fiona.open(input_file) as input_features:
        remove_fields_from_features(input_features, dropped_fields.split(','))


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        args = sys.argv
        main(sys.argv[1], sys.argv[2])
    else:
        raise SyntaxError("Invalid number of arguments.")
