# Download and Unzip all Microsoft Building Footprint Data
echo Downloading Microsoft Building Footprint Data
mkdir ms
cd ms

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/Alberta.zip
unzip Alberta.zip -d ab

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/BritishColumbia.zip
unzip BritishColumbia.zip -d bc

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/Manitoba.zip
unzip Manitoba.zip -d mb

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/NewBrunswick.zip
unzip NewBrunswick.zip -d nb

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/NewfoundlandAndLabrador.zip
unzip NewfoundlandAndLabrador.zip -d nl

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/NorthwestTerritories.zip
unzip NorthwestTerritories.zip -d nt

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/NovaScotia.zip
unzip NovaScotia.zip -d ns

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/Nunavut.zip
unzip Nunavut.zip -d nu

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/Ontario.zip
unzip Ontario.zip -d on

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/PrinceEdwardIsland.zip
unzip PrinceEdwardIsland.zip -d pe

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/Quebec.zip
unzip Quebec.zip -d qc

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/Saskatchewan.zip
unzip Saskatchewan.zip -d sk

wget https://usbuildingdata.blob.core.windows.net/canadian-buildings-v2/YukonTerritory.zip
unzip YukonTerritory.zip -d yt

# Download and Unzip all Open Street Maps Open Building Footprint Data
echo Downloading Open Street Maps Building Footprint Data from GeoFabriks
mkdir ../osm
cd ../osm

wget http://download.geofabrik.de/north-america/canada/alberta-latest-free.shp.zip
mkdir ab
unzip alberta-latest-free.shp.zip -d tempab
cp tempab/gis_osm_buildings* ab/.
rm -rf tempab

wget http://download.geofabrik.de/north-america/canada/british-columbia-latest-free.shp.zip
mkdir bc
unzip british-columbia-latest-free.shp.zip -d tempbc
cp tempbc/gis_osm_buildings* bc/.
rm -rf tempbc

wget http://download.geofabrik.de/north-america/canada/manitoba-latest-free.shp.zip
mkdir mb
unzip manitoba-latest-free.shp.zip -d tempmb
cp tempmb/gis_osm_buildings* mb/.
rm -rf tempmb

wget http://download.geofabrik.de/north-america/canada/new-brunswick-latest-free.shp.zip
mkdir nb
unzip new-brunswick-latest-free.shp.zip -d tempnb
cp tempnb/gis_osm_buildings* nb/.
rm -rf tempnb

wget http://download.geofabrik.de/north-america/canada/newfoundland-and-labrador-latest-free.shp.zip
mkdir nl
unzip newfoundland-and-labrador-latest-free.shp.zip -d tempnl
cp tempnl/gis_osm_buildings* nl/.
rm -rf tempnl

wget http://download.geofabrik.de/north-america/canada/northwest-territories-latest-free.shp.zip
mkdir nt
unzip northwest-territories-latest-free.shp.zip -d tempnt
cp tempnt/gis_osm_buildings* nt/.
rm -rf tempnt

wget http://download.geofabrik.de/north-america/canada/nova-scotia-latest-free.shp.zip
mkdir ns
unzip nova-scotia-latest-free.shp.zip -d tempns
cp tempns/gis_osm_buildings* ns/.
rm -rf tempns

wget http://download.geofabrik.de/north-america/canada/nunavut-latest-free.shp.zip
mkdir nu
unzip nunavut-latest-free.shp.zip -d tempnu
cp tempnu/gis_osm_buildings* nu/.
rm -rf tempnu

wget http://download.geofabrik.de/north-america/canada/ontario-latest-free.shp.zip
mkdir on
unzip ontario-latest-free.shp.zip -d tempon
cp tempon/gis_osm_buildings* on/.
rm -rf tempon

wget http://download.geofabrik.de/north-america/canada/prince-edward-island-latest-free.shp.zip
mkdir pe
unzip prince-edward-island-latest-free.shp.zip -d temppe
cp temppe/gis_osm_buildings* pe/.
rm -rf temppe

wget http://download.geofabrik.de/north-america/canada/quebec-latest-free.shp.zip
mkdir qc
unzip quebec-latest-free.shp.zip -d tempqc
cp tempqc/gis_osm_buildings* qc/.
rm -rf tempqc

wget http://download.geofabrik.de/north-america/canada/saskatchewan-latest-free.shp.zip
mkdir sk
unzip saskatchewan-latest-free.shp.zip -d tempsk
cp tempsk/gis_osm_buildings* sk/.
rm -rf tempsk

wget http://download.geofabrik.de/north-america/canada/yukon-latest-free.shp.zip
mkdir yt
unzip yukon-latest-free.shp.zip -d tempyt
cp tempyt/gis_osm_buildings* yt/.
rm -rf tempyt

# Download and Unzip all Open Database of Buildings Data
echo Downloading ODB Data from Statistics Canada
mkdir ../odb
cd ../odb

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_Alberta.zip
unzip ODB_v2_Alberta.zip -d ab

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_BritishColumbia.zip
unzip ODB_v2_BritishColumbia.zip -d bc

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_NewBrunswick.zip
unzip ODB_v2_NewBrunswick.zip -d nb

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_NorthwestTerritories.zip
unzip ODB_v2_NorthwestTerritories.zip -d nt

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_NovaScotia.zip
unzip ODB_v2_NovaScotia.zip -d ns

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_Ontario.zip
unzip ODB_v2_Ontario.zip -d on

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_Quebec.zip
unzip ODB_v2_Quebec.zip -d qc

wget https://www150.statcan.gc.ca/n1/pub/34-26-0001/2018001/ODB_v2_Saskatchewan.zip
unzip ODB_v2_Saskatchewan.zip -d sk

# Download CSD Data
echo Downloading Census Subdivision Data
mkdir ../lcsd000b16a_e
cd ../lcsd000b16a_e
wget --no-check-certificate https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lcsd000b16a_e.zip
unzip lcsd000b16a_e.zip

# Download Prov/Terr Boundary Data
echo Downloading Province and Territory Boundary Data
mkdir ../lpr_000a16a_e
cd ../lpr_000a16a_e
wget --no-check-certificate http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lpr_000a16a_e.zip
unzip lpr_000a16a_e.zip

