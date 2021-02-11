rm -f merge/output/*

# Process Alberta Data:
echo Processing Alberta data ...
python Merge.py ab ../data/odb/ab/ODB_Alberta/odb_alberta.shp ../data/osm/ab/gis_osm_buildings_a_free_1.shp ../data/ms/ab/Alberta.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/ab_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process British Columbia Data:
echo Processing British Columbia data ...
python Merge.py bc ../data/odb/bc/ODB_BritishColumbia/odb_britishcolumbia.shp ../data/osm/bc/gis_osm_buildings_a_free_1.shp ../data/ms/bc/BritishColumbia.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/bc_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Manitoba Data:
echo Processing Manitoba data ...
python Merge.py mb ../data/osm/mb/gis_osm_buildings_a_free_1.shp ../data/ms/mb/Manitoba.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/mb_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process New Brunswick Data:
echo Processing New Brunswick data ...
python Merge.py nb ../data/odb/nb/ODB_NewBrunswick/odb_newbrunswick.shp ../data/osm/nb/gis_osm_buildings_a_free_1.shp ../data/ms/nb/NewBrunswick.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/nb_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Newfoundland and Labrador Data:
echo Processing Newfoundland and Labrador data ...
python Merge.py nl ../data/osm/nl/gis_osm_buildings_a_free_1.shp ../data/ms/nl/NewfoundlandAndLabrador.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/nl_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Nova Scotia Data:
echo Processing Nova Scotia data ...
python Merge.py ns ../data/odb/ns/ODB_NovaScotia/odb_novascotia.shp ../data/osm/ns/gis_osm_buildings_a_free_1.shp ../data/ms/ns/NovaScotia.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/ns_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Northwest Territories Data:
echo Processing Northwest Territories data ...
python Merge.py nt ../data/odb/nt/ODB_NorthwestTerritories/odb_northwestterritories.shp ../data/osm/nt/gis_osm_buildings_a_free_1.shp ../data/ms/nt/NorthwestTerritories.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/nt_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Nunavut Data:
echo Processing Nunavut data ...
python Merge.py nu ../data/osm/nu/gis_osm_buildings_a_free_1.shp ../data/ms/nu/Nunavut.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/nu_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Ontario Data:
echo Processing Ontario data ...
python Merge.py on ../data/odb/on/ODB_Ontario/odb_ontario.shp ../data/osm/on/gis_osm_buildings_a_free_1.shp ../data/ms/on/Ontario.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/on_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Prince Edward Island Data:
echo Processing Prince Edward Island data ...
python Merge.py pe ../data/osm/pe/gis_osm_buildings_a_free_1.shp ../data/ms/pe/PrinceEdwardIsland.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/pe_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Quebec Data:
echo Processing Quebec data ...
python Merge.py qc ../data/odb/qc/ODB_Quebec/odb_quebec.shp ../data/osm/qc/gis_osm_buildings_a_free_1.shp ../data/ms/qc/Quebec.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/qc_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Saskatchewan Data:
echo Processing Saskatchewan data ...
python Merge.py sk ../data/odb/sk/ODB_Saskatchewan/odb_saskatchewan.shp ../data/osm/sk/gis_osm_buildings_a_free_1.shp ../data/ms/sk/Saskatchewan.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/sk_odb_osm_ms.zip merge/output/
rm -f merge/output/*

# Process Yukon Territory Data:
echo Processing Yukon data ...
python Merge.py yt ../data/osm/yt/gis_osm_buildings_a_free_1.shp ../data/ms/yt/YukonTerritory.geojson ../data/lcsd000b16a_e/lcsd000b16a_e.shp

zip -ro merge/yt_odb_osm_ms.zip merge/output/
rm -f merge/output/*

