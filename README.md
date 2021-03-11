# Integrated Canadian Building Footprints (ICBF)
This is the project directory containing the scripts needed to download, process, and produce updated Mapbox tiles for Canadian building footprint data, sourced from the [Open Database of Buildings (ODB)](https://www.statcan.gc.ca/eng/lode/databases/odb), [Microsoft Canadian Building Footprints](https://github.com/microsoft/CanadianBuildingFootprints), and [OpenSteetMap (OSM)](https://www.geofabrik.de/).

The scripts in this project are broken up into workflow tasks, and contain both the original Python scripts and Bash scripts that provide an example of how they can be used. 

The script and documentation are part of work in progress and subject to continuous development. The technical documentation is available in English only.

# Empreintes intégrées des immeubles canadiens (EIIC)

Voici le répertoire pour les scripts nécessaires afin de télécharger, traiter et produire des tuiles Mapbox mises à jour pour les données sur l'empreinte des immeubles canadiens, provenant de [la Base de données ouvertes sur les immeubles (BDOI)](https://www.statcan.gc.ca/fra/ecdo/bases-donnees/bdoi), [les empreintes de bâtiments Microsoft](https://github.com/microsoft/CanadianBuildingFootprints), et [OpenSteetMap (OSM)](https://www.geofabrik.de/).

Les scripts de ce projet sont divisés en tâches de flux de travail et contiennent à la fois les scripts Python originaux et les scripts Bash qui fournissent un exemple de leur utilisation.

Le script et la documentation font partie du travail en cours et font l'objet d'un développement continu. La documentation technique est disponible en anglais uniquement.

--------
## Directory Structure:
```
/
├───data - contains script for downloading all data.
├───mbtiles - contains script for converting geojsons to mbtiles
├───merge - contains scripts for merging ODB, OSM, and MS data
├───minifying - contains scripts for minimizing merged geojson files
├───preprocessing - contains scripts for preprocessing OSM and MS data
├───statistics - contains a script and results for calculating stats on output
├───utils - contains utility scripts
└───validation - contains scripts for sampling data used for validation and quality control.
```

--------
## Processing Workflow:
The general steps for process:

1. Download open building footprint spatial data and spatial boundary data.
2. Preprocessing the OSM and MS data.
3. Merging ODB, OSM and MS data using GeoPandas.
4. Minifying the merge data. 
 * Removing all fields but the required data provider 'Data_prov', reducing the coordinate precision from 15 to 7 decimal places, and remove duplicate geometries. This resulted in a significan reduction of the data size requirements.
5. Conversion of the minified geojson data into Mapbox tiles data (.mbtiles files)
6. Scripts for sampling the data to perform a validation assessment


--------
## Processing requirements:

* Python 3.6+
* geopandas
* tqdm
* spatialy
* fiona
* pygeos
* tippecanoe
* Linux environment for running bash scripts (optional)
* +20Gb of hardrive space
* Internet connection for downloading building spatial data.


------
## 1. Downloading Open Data:
The Building Footprints project requires data from a variety of sources, and can be downloaded with the provided bash script.

### Downloaded Data:
Building data is downloaded from:

* [Open Database of Buildings (ODB)](https://www.statcan.gc.ca/eng/lode/databases/odb)
* [OpenStreetMap (OSM)](https://www.geofabrik.de/)
* [Microsoft (MS)](https://github.com/microsoft/CanadianBuildingFootprints)

Boundary Data is downloaded from:

* [2016 Census Subdivisions Boundary File](https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lcsd000b16a_e.zip)
* [2016 Province/Territory Boundary File](http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lpr_000a16a_e.zip)

### How To Download The Data:
To simplify this process of downloading the required data, a bash script was created to automate this process (see ./data/download_open_building_footprints.sh). To download all of the required data for this project, simply modify the bash script to be executable (e.g. `chmod u+x download_open_building_footprints.sh`) and then run the script `./download_open_building_footprints.sh` in the terminal from the data directory.

Alternatively, you could also manually download each file separately.

------
## 2. Preprocessing Open Data:
### Why preprocess the data?:
During quality control of the source data it was noticed that MS and OSM building footprint data had inconsistencies near province/territory borders. For example, a duplicate of data in a province can also exist in another province's data near a border, and also data associated with one province can overlap another province's area.

The solution to this is to preprocess the data, by combining all of the Canadian building footprints per datasource (OSM or MS), re-dividing it using established spatial boundaries for each province/territory, and removing any duplicates. This should ensure that only unique data contained in each province/territory is included for the specific province/territory. 

### Steps for preprocessing:

1. Copy scripts from `./preprocessing` directory`
2. Create a Python Environment and install script dependencies if they aren't available.
 * `python -m venv venv`
 * `source venv\bin\activate`
 * `pip install geopandas`
 * `pip install pygeos`
 * `pip install tqdm`
3. Create an `output` directory in the same folder as the preprocessing scripts
4. Ensure a copy of boundary lpr_000a16a_e.* shape files is accessible by the script (e.g. copy the boundary shape files to the script's directory)
5. Create an `input` directory
6. Create an `osm` directory within the `input` directory, and copy all OSM shape files to the directory. (Note: Geofabrik names all their building shape files the same, so you will need to provide unique names for each shape file (e.g. add a prov/terr abbreviation prefix to each file).
7. Create an `ms` directory within the `input` directory, and copy all MS GeoJSON files to the directory.
8. Make sure the `merge_and_split_preprocessing.sh` bash script is executable (e.g. `chmod u+x <file-name>`)
9. Run the `merge_and_split_prepocessing.sh` script in a terminal, or run the python script manually (Example: `python merge_and_split.py input/ms split/lpr_000a16a_e.shp PRUID`).
10. Copy preprocessed zipped data for use in the next step (3. Merging).


------
## 3. Merging ODB, OSM, and MS Data:

The merge scripts performs the following operations on the datasets. It combines the ODB, OSM and MS building footprints, which follows a hierarchy of ODB > OSM > MS. I.e. if an ODB building feature overlaps with an OSM and/or MS feature, the ODB feature is retained and the OSM and/or MS feature is excluded from the final product. Also if the OSM overlaps with a MS feature the MS Feature is excluded, and if an ODB or OSM or MS feature is spatially isolated it will be included in the final combined product.

In addition, the script also associates Census Subdivision data to each building footprint, and calculates geometry information for each feature (e.g. area and length). 

The final output is a merged building footprints GeoJSON file for each province/territory. 

## Steps to run building footprint merge processing:

1. Create a Python Environment and install script dependencies.
 * `python -m venv venv`
 * `source venv\bin\activate`
 * `pip install geopandas`
 * `pip install pygeos`
2. Update provided bash script `odb_osm_ms_building_footprint_merge.sh` with ODB, OSM, MS, CSD data file paths (if using the script). Note: Make sure to copy the data from the preprocessing step to a location you have access to for this script.
3. If the provided bash script is being used, ensure that the bash script is executable. If it's not, use `chmod u+x odb_osm_ms_building_footprint_merge.sh` to make it executable. 
4. Run script that processes the merging of Canadian building footprints using the sources ODB, OSM, and MS, by typing `./odb_osm_ms_building_footprint_merge.sh` in the terminal. Alternatively you can also run the Merge.py script directly and provide the required CLI arguments prov/terr abbreviation, ODB data, OSM, data, MS data, and CSD data sources. Example: `python Merge.py ab ../data/odb/ab/ODB_Alberta/odb_alberta.shp ../data/osm/AB.geojson ../data/ms/AB.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp`.
 * A geojson file for each province/territory is exported by the merge script which is compressed as a zip file, and saved in the `merge/` directory by bash script.
 
Note: All OSM building data is merged into the merged datasets due to not knowing what future applications are needed for this data. This includes polygons that represent parts of a building (e.g. buildings of type == roof). If portions of buildings are not required for your application, you may want to filter out/remove these rows of data from each dataset.
 

-------
## 4. Minify GeoJSON Data (optional):
When the merged GeoJSON files from step 3 are too big they will also result in large MBTiles. To reduce the MBTiles size, the GeoJSON data needs to be reduced through a combination of removing any duplicate geometries in the merged dataset, limiting the coordinate precision to 7 decimal places (more than sufficient for this application), and removing extra fields in the data.

1. Create a Python Environment and install script dependencies if they aren't available.
 * `python -m venv venv`
 * `source venv\bin\activate`
 * `pip install geopandas`
 * `pip install pygeos`
 * `pip install fiona`
 * `pip install shapely`
 * `pip install tqdm`
2. By running the `./minifying/reduce_coordinate_precision.py` script, coordinate precision can be reduced on a GeoJSON file to a specified level. Initially the coordinate precision for the processed geojson files was 15 decimal places, which was reduced to 7 using the provided bash script in the `./minifying` directory. This step csn also be performed with the Python script for each merged file by specifying the input data, and the coordinate precision (Example: `python reduce_coordinate_precision.py input.geojson 7`).
3. Using the `remove_fields_from_geojson.py` script, specified fields can be removed from the GeoJSON file. This approach provides the largest file size reduction. This step can be performed with the Python script for each merged file by specifying the input data file, and a quoted list of field names (Example: `python remove_fields_from_geojson.py input.geojson "Build_ID,Shape_Leng,Shape_Area"`).
4. Lastly the `./minifying/remove_duplicate_geometries.py` script, ensures only unique geometries for each province were kept. Note: this step should be done after the field removals step.  This step can be performed with the Python script for each merged file (Example: `python remove_duplicate_geometries.py input.geojson`).

Note: To see an example of each scripts usage, see the `./minifying/minify_merged_building_footprint_data.sh` bash script.

 
---------
## 5. Convert Minified Merged GeoJSON files Into MBTiles:

Final step in this work flow is converting the minified GeoJSON files from the previous step into mbtiles (Note: In the case of Ontario, the original data was too large to upload, and was split in two).

1. Install tippecanoe:
 **Steps for setting up a conda environment with tippecanoe in JuptyerLab**
  1. Create a new environment 
   * type "conda create --name tippe" in terminal
  2. Make sure conda is initalized with bash as it's terminal
   * type "conda init bash" in terminal
  3. Make sure bash is being used 
   * type "bash" in terminal
  4. Activate the conda environment created in step 1.
   * type "conda activate tippe" in terminal
  5. Install tippecanoe in environment
   * type "conda install -c conda-forge tippecanoe"
  6. Run tippecanoe processes. e.g. this bash script
  7. When finished deactivate environment
   * type "conda deactivate" in terminal
   
2. Move zipped GeoJSON output from the building footprint merge process (or minified step if performed) to an accessible folder, and unzip the data.
3. Move `./mbtiles/building_footprints_mbtiles_processing.sh` to the same directory as the one used in the previous step.
4. Update the bash script with the updated input or output names (if required) or run the following tippecanoe command on the available GeoJSON file(s), e.g. `tippecanoe -z15 -Z10 -o ./buildings_qc.mbtiles --force --drop-densest-as-needed QC.geojson`
5. Run the script on the GeoJSON files


----------
## 6. Sampling data for Validation:
You may want to perform some validation of the data you've merged to ensure its accuracy. The following steps can provide methods of sampling the output data for visual assessment in a GIS:

1. Create a Python Environment and install script dependencies if they aren't available.
 * `python -m venv venv`
 * `source venv\bin\activate`
 * `pip install geopandas`
 * `pip install pygeos`
2. Run the script that randomly samples each province for generating a sub-set of the data for validation.
 * Update `validation/odb_osm_ms_building_footprint_sample.sh` data paths if required.
 * Run the `validation/odb_osm_ms_building_footprint_sample.sh`
 * Output from the script will be stored as a compressed zip file saved in the validation/ directory.
 * Note: Sampling threshold by default is 5%, but can be modified in the `Random_Sampling.py` script.
3. If additional samples are needed for specific metro areas (CMAs), a modified `Random_Sampling_By_CMA.py` was created for this purpose.
 * Update and run the `validation/odb_osm_ms_building_footprint_sample_by_cma.sh` for sampling a specified number of CSDs from specified CMAs. 
 * Note: The CMA ID and number of CSDs to sample can be updated in this bash script, `python Random_Sampling_By_CMA.py <cma-id> <amount-of-csd> <merged-processed-data.geojson>` E.g `python Random_Sampling_By_CMA.py 825 2 merge/output/odb_osm_ms_merged_building_footprints_AB.geojson`

Note: Additional Python scripts, `./validation/Extract_By_CSDUID.py` and `./validation/Clip_DF.py`, were provided for extracting test data from GeoJSON. Neither script is required for the above validation scripts, but both can be useful for extracting a small sample of data for testing/assessment purposes, since the original/processed data can be cumbersome to work with.
