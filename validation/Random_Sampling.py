"""
Sample building footprint data by randomnly selecting Census Subdivisions
in a province/territory. Sampled data is exported, and this process continues
until a sample threshold is reached.
"""
import time
import random
import math
import os.path
import sys
import geopandas as gpd


def main(region, bf_file, csd_file):
    """
    Main entry point for application

    Attributes
    ----------
    region: str
        A two character province or territory code (e.g. NU, PE, NB, etc).
    bf_file: str
        File location for building footprints.
    csd_file: str
        File location for census subdivision file.
    """

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

    start_time = time.time()
    pr_terr_abrv = None

    # Check if region is valid
    if region.upper() in list(prov_terr_id_map.keys()):
        pr_terr_abrv = region.upper()

    # 5% threshold
    threshold_percentage = 0.05

    randomly_selected_csd = []
    sample_size = 0

    # If the arguments are valid proceed with sampling of data
    if pr_terr_abrv and os.path.exists(bf_file) and os.path.exists(csd_file):
        pr_terr_id = prov_terr_id_map[pr_terr_abrv]

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

        # Query CSD features for the province/territory being processed
        print("Querying Census Subdivision Dataset to Only include features in selected {}".format(pr_terr_abrv))
        csd = csd[csd['PRUID'] == pr_terr_id]

        # Drop all but CSDUID, CSDNAME, and geometry fields from csd
        csd = csd[['CSDUID', 'CSDNAME', 'geometry']]

        # Randomnly select CSDs:
        while sample_size < total_size * threshold_percentage:
            random_csd = math.floor(random.random() * len(csd.geometry))
            random_csd_row = csd.iloc[random_csd]
            random_csd_id = random_csd_row['CSDUID']

            # Ensure no csd is selected more than once
            if random_csd_id not in randomly_selected_csd:
                randomly_selected_csd.append(random_csd_id)

                # Export all building features for each randomnly selected csd
                print('Exporting CSD ' + random_csd_id + ' building footprints')
                csd_subselection = bf[bf['CSDUID'] == random_csd_id]
                sample_size += len(csd_subselection.geometry)

                if not csd_subselection.empty:
                    csd_subselection.to_file('validation/output/'+random_csd_id+'_'+pr_terr_abrv+'.geojson', driver = 'GeoJSON')

    # -------------------------------------------------
    end_time = time.time()

    print("Time to complete processing: {} mins".format((end_time - start_time) / 60))


if __name__ == "__main__":
    if len(sys.argv) == 4:
        args = sys.argv
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        raise SyntaxError("Invalid number of arguments.")
