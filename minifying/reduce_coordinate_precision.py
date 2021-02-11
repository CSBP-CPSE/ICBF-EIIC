"""
A geospatial script to reduce coordinate precision of all geospatial features.
"""
import sys
import fiona
import shapely.geometry
import shapely.wkt
from tqdm import tqdm


def reduce_coordinate_precision(input_features, coord_precision):
    """
    Reduces the coordinate precision of the input features to the specified amount.

    :param input_features {string} - File location of the input data.
    :param coord_precision {number} - number of decimal places to keep in coordinates
    """

    output_file = input_features.name + '_reduce_coord_precision.geojson'
    with fiona.open(output_file, 'w', driver='GeoJSON', crs=input_features.crs, schema=input_features.schema) as output:
        for elem in tqdm(input_features, position=0, leave=True):
            elem_geom = shapely.geometry.shape(elem['geometry'])

            # Reduce precision of coordinate geometry
            reduced_geom = shapely.wkt.loads(shapely.wkt.dumps(elem_geom, rounding_precision=coord_precision))

            # Output geometries with reduced coordinate precision
            output.write({
                'geometry': shapely.geometry.mapping(reduced_geom),
                'properties': elem['properties']
            })

        print("Finished reducing coordinate precision for {}".format(input_features.name))


def main(input_file, coord_precision):
    """
    Entry point of coordinate precision reduction script

    Attributes:
    ---------------
    :param input_file {string} - Path to input file
    :param coord_precision {number} - Number of decimal places to reduce coordinate precision to
    """

    print("Opening input data...")
    with fiona.open(input_file) as input_features:
        print("Reducing input features coordinate precision")
        reduce_coordinate_precision(input_features, coord_precision)


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        args = sys.argv
        main(sys.argv[1], sys.argv[2])
    else:
        raise SyntaxError("Invalid number of arguments.")
