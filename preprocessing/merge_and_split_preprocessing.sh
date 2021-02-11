# Preprocess ms files
# Notes: 
# - All ms geojson files are stored in the input/ms directory 
# - Prov/Terr boundary file for spliting data is stored in the split/ directory
python merge_and_split.py input/ms split/lpr_000a16a_e.shp PRUID

# Zip up preprocess output
zip preprocessed_ms.zip output/*.geojson

# Remove old output
rm output/*.geojson


# Preprocess osm files
# Notes: 
# - All osm shape files are stored in the input/osm directory 
# - Prov/Terr boundary file for spliting data is stored in the split/ directory
python merge_and_split.py input/osm split/lpr_000a16a_e.shp PRUID

# Zip up preprocess output
zip preprocessed_osm.zip output/*.geojson

# Remove old output
rm output/*.geojson
