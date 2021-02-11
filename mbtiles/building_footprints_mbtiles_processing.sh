# Steps for setting up a conda environment with tippecanoe in JuptyerLab
# 1. Create a new environment 
#  * type "conda create --name tippe" in terminal
# 2. Make sure conda is initalized with bash as it's terminal
#  * type "conda init bash" in terminal
# 3. Make sure bash is being used 
#  * type "bash" in terminal
# 4. Activate the conda environment created in step 1.
#  * type "conda activate tippe" in terminal
# 5. Install tippecanoe in environment
#  * type "conda install -c conda-forge tippecanoe"
# 6. Run tippecanoe processes. e.g. this bash script
# 7. When finished deactivate environment
#  * type "conda deactivate" in terminal

# Remove old mbtiles files
rm *.mbtiles
rm *.mbtiles-journal

# Create mbtiles for NB, NL, NS, and PE.
tippecanoe -z15 -Z10 -o ./buildings_nb_nl_ns_pe.mbtiles --force --drop-densest-as-needed NB.geojson NL.geojson NS.geojson PE.geojson

# Create mbtiles for NT, MB, and SK.
tippecanoe -z15 -Z10 -o ./buildings_nt_mb_sk.mbtiles --force --drop-densest-as-needed NT.geojson MB.geojson SK.geojson

# Create mbtiles for AB, BC, YT.
tippecanoe -z15 -Z10 -o ./buildings_ab_bc_yt.mbtiles --force --drop-densest-as-needed AB.geojson BC.geojson YT.geojson

# Create mbtiles for QC, NU.
tippecanoe -z15 -Z10 -o ./buildings_qc_nu.mbtiles --force --drop-densest-as-needed QC.geojson NU.geojson

# Create mbtiles for ON Part 1.
tippecanoe -z15 -Z10 -o ./buildings_on_pt1.mbtiles --force --drop-densest-as-needed ON_pt1.geojson

# Create mbtiles for ON Part 2.
tippecanoe -z15 -Z10 -o ./buildings_on_pt2.mbtiles --force --drop-densest-as-needed ON_pt2.geojson
