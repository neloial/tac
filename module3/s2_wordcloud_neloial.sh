#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR=$1
cat "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/txt/*_${YEAR}_*.txt > "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/${YEAR}.txt
python3 module3/filtering_neloial.py '/Volumes/Extreme SSD/Temp/TPTraitAuto/data' $YEAR
wordcloud_cli --text "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/${YEAR}_keywords.txt --imagefile "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/${YEAR}.png --width 2000 --height 1000
display "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/${YEAR}.png
