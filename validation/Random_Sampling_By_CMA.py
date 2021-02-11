"""
Sample building footprint data by randomnly selecting Census Subdivisions
in a CMA. Sampled data is exported, and this process continues
until a sample threshold is reached.
"""
import time
import random
import math
import os.path
import sys
import geopandas as gpd


def main(cmauid, samples, bf_file, csd_file):
    """
    Main entry point for application

    Attributes
    ----------
    cmauid: str
        A CMAUID (e.g. 462).
    bf_file: str
        File location for building footprints.
    csd_file: str
        File location for census subdivision file.
    """

    start_time = time.time()
    randomly_selected_csd = []
    sample_size = 0
    max_sample_size = int(samples)

    # If the arguments are valid proceed with sampling of data
    if cmauid and os.path.exists(bf_file) and os.path.exists(csd_file):

        # -------------------------------------------------
        # Load each dataset
        # -------------------------------------------------
        # Read Building Footprints dataset
        print("Reading Building Footprints Dataset ...")
        bf = gpd.read_file(bf_file)
        total_size = len(bf.geometry)

        # Read CSD dataset
        print("Reading Census Subdivision Dataset ...")
        csd = gpd.read_file(csd_file)

        # Query CSD features for the specified cma being processed
        print("Querying Census Subdivision Dataset to Only include features in selected {}".format(cmauid))
        csd = csd[csd['CMAUID'] == cmauid]

        # Drop all but CSDUID, CSDNAME, and geometry fields from csd
        csd = csd[['CSDUID', 'CSDNAME', 'geometry']]

        # Randomnly select CSDs:
        while sample_size < max_sample_size:
            random_csd = math.floor(random.random() * len(csd.geometry))
            random_csd_row = csd.iloc[random_csd]
            random_csd_id = random_csd_row['CSDUID']

            # Ensure no csd is selected more than once
            if random_csd_id not in randomly_selected_csd:
                randomly_selected_csd.append(random_csd_id)

                # Export all building features for each randomnly selected csd
                print('Exporting CSD ' + random_csd_id + ' building footprints')
                csd_subselection = bf[bf['CSDUID'] == random_csd_id]
                sample_size += 1 

                if not csd_subselection.empty:
                    csd_subselection.to_file('validation/output/'+random_csd_id+'_'+cmauid+'.geojson', driver = 'GeoJSON')

    # -------------------------------------------------
    end_time = time.time()

    print("Time to complete processing: {} mins".format((end_time - start_time) / 60))


if __name__ == "__main__":
    if len(sys.argv) == 5:
        args = sys.argv
        main(str(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        raise SyntaxError("Invalid number of arguments.")
