#!/usr/bin/env bash

# Converting PDFs to text files and moving them to a new directory

for file in "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/pdf/*.pdf; do pdftotext -enc UTF-8 "$file" "${file%.*}.txt"; done
mkdir "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/txt
mv "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/pdf/*.txt "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/txt/
ls "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/txt | wc -l
cat "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/txt/*.txt > "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/all.txt
wc "/Volumes/Extreme SSD/Temp/TPTraitAuto/"data/all.txt
