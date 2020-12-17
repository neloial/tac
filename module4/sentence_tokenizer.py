"""Tokenize sentences"""

import os
import sys
import nltk
from nltk.tokenize import sent_tokenize

nltk.data.path.append("/Volumes/Extreme SSD/Temp/TPTraitAuto/nltk_data")

infile = f"/Volumes/Extreme SSD/Temp/TPTraitAuto/data/all.txt"
outfile = f"/Volumes/Extreme SSD/Temp/TPTraitAuto/data/sents.txt"

with open(outfile, 'w', encoding="utf-8") as output:
    with open(infile, encoding="utf-8", errors="backslashreplace") as f:
        for line in f:
            sentences = sent_tokenize(line)
            for sent in sentences:
                output.write(sent + "\n")
