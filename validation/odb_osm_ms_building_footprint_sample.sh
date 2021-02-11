rm -f merge/output/*
rm -f validation/output/*

# Sampling Alberta Data:
echo Sampling Alberta data ...
cp merge/ab_odb_osm_ms.zip .
unzip ab_odb_osm_ms.zip
rm ab_odb_osm_ms.zip
python Random_Sampling.py AB merge/output/odb_osm_ms_merged_building_footprints_AB.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/ab_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling British Columbia Data:
echo Sampling British Columbia data ...
cp merge/bc_odb_osm_ms.zip .
unzip bc_odb_osm_ms.zip
rm bc_odb_osm_ms.zip
python Random_Sampling.py BC merge/output/odb_osm_ms_merged_building_footprints_BC.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/bc_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Manitoba Data:
echo Sampling Manitoba data ...
cp merge/mb_odb_osm_ms.zip .
unzip mb_odb_osm_ms.zip
rm mb_odb_osm_ms.zip
python Random_Sampling.py MB merge/output/odb_osm_ms_merged_building_footprints_MB.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/mb_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling New Brunswick Data:
echo Sampling New Brunswick data ...
cp merge/nb_odb_osm_ms.zip .
unzip nb_odb_osm_ms.zip
rm nb_odb_osm_ms.zip
python Random_Sampling.py NB merge/output/odb_osm_ms_merged_building_footprints_NB.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/nb_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Newfoundland And Labrador Data:
echo Sampling Newfoundland And Labrador data ...
cp merge/nl_odb_osm_ms.zip .
unzip nl_odb_osm_ms.zip
rm nl_odb_osm_ms.zip
python Random_Sampling.py NL merge/output/odb_osm_ms_merged_building_footprints_NL.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/nl_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Nova Scotia Data:
echo Sampling Nova Scotia data ...
cp merge/ns_odb_osm_ms.zip .
unzip ns_odb_osm_ms.zip
rm ns_odb_osm_ms.zip
python Random_Sampling.py NS merge/output/odb_osm_ms_merged_building_footprints_NS.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/ns_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Northwest Territories Data:
echo Sampling Northwest Territories data ...
cp merge/nt_odb_osm_ms.zip .
unzip nt_odb_osm_ms.zip
rm nt_odb_osm_ms.zip
python Random_Sampling.py NT merge/output/odb_osm_ms_merged_building_footprints_NT.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/nt_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Nunavut Data:
echo Sampling Nunavut data ...
cp merge/nu_odb_osm_ms.zip .
unzip nu_odb_osm_ms.zip
rm nu_odb_osm_ms.zip
python Random_Sampling.py NU merge/output/odb_osm_ms_merged_building_footprints_NU.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/nu_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Ontario Data:
echo Sampling Ontario data ...
cp merge/on_odb_osm_ms.zip .
unzip on_odb_osm_ms.zip
rm on_odb_osm_ms.zip
python Random_Sampling.py ON merge/output/odb_osm_ms_merged_building_footprints_ON.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/on_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Prince Edward Island Data:
echo Sampling Prince Edward Island data ...
cp merge/pe_odb_osm_ms.zip .
unzip pe_odb_osm_ms.zip
rm pe_odb_osm_ms.zip
python Random_Sampling.py PE merge/output/odb_osm_ms_merged_building_footprints_PE.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/pe_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Quebec Data:
echo Sampling Quebec data ...
cp merge/qc_odb_osm_ms.zip .
unzip qc_odb_osm_ms.zip
rm qc_odb_osm_ms.zip
python Random_Sampling.py QC merge/output/odb_osm_ms_merged_building_footprints_QC.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/qc_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Saskatchewan Data:
echo Sampling Saskatchewan data ...
cp merge/sk_odb_osm_ms.zip .
unzip sk_odb_osm_ms.zip
rm sk_odb_osm_ms.zip
python Random_Sampling.py SK merge/output/odb_osm_ms_merged_building_footprints_SK.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/sk_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

# Sampling Yukon Data:
echo Sampling Yukon data ...
cp merge/yt_odb_osm_ms.zip .
unzip yt_odb_osm_ms.zip
rm yt_odb_osm_ms.zip
python Random_Sampling.py YT merge/output/odb_osm_ms_merged_building_footprints_YT.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro validation/yt_validation_sample.zip validation/output
rm -f validation/output/*
rm -f merge/output/*

