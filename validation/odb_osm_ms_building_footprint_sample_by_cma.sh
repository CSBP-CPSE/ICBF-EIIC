rm -f merge/output/*
rm -f validation/output/*

# Sampling Alberta Data:
echo Sampling Alberta data ...
cp merge/ab_odb_osm_ms.zip .
unzip ab_odb_osm_ms.zip
rm ab_odb_osm_ms.zip
python Random_Sampling_By_CMA.py 825 2 merge/output/odb_osm_ms_merged_building_footprints_AB.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -r validation/ab_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling British Columbia Data:
echo Sampling British Columbia data ...
cp merge/bc_odb_osm_ms.zip .
unzip bc_odb_osm_ms.zip
rm bc_odb_osm_ms.zip
python Random_Sampling_By_CMA.py 933 2 merge/output/odb_osm_ms_merged_building_footprints_BC.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -r validation/bc_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Ontario Data:
echo Sampling Ontario data ...
cp merge/on_odb_osm_ms.zip .
unzip on_odb_osm_ms.zip
rm on_odb_osm_ms.zip
python Random_Sampling_By_CMA.py 535 3 merge/output/odb_osm_ms_merged_building_footprints_ON.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -r validation/on_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Quebec Data:
echo Sampling Quebec data ...
cp merge/qc_odb_osm_ms.zip .
unzip qc_odb_osm_ms.zip
rm qc_odb_osm_ms.zip
python Random_Sampling_By_CMA.py 462 3 merge/output/odb_osm_ms_merged_building_footprints_QC.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -r validation/qc_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

