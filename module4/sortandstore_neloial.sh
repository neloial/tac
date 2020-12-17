#!/usr/bin/env bash

# Capture the output of clustering in a separate file and
# Copy the files from txt to a cluster folder

mkdir "/Volumes/Extreme SSD/Temp/TPTraitAuto/data/txt/cluster/"
DECADE=$1
python3 module4/clustering_neloial.py $DECADE > "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/txt/cluster/${DECADE}.txt