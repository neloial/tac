"""Analyse frequency distribution of words"""

import nltk
import os
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout", 
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu"]
sw = set(sw)
print(f"{len(sw)} stopwords used: {sorted(sw)}")

path = "/Volumes/Extreme SSD/Temp/TPTraitAuto/data/all.txt"
#limit = 10**8

with open(path) as f:
    text = f.read()
    words = nltk.wordpunct_tokenize(text)
    print(f"{len(words)} words found")
    #kept = [w.lower() for w in words if len(w) > 2 and w.isalpha() and w.lower() not in sw]
    kept = [w.lower() for w in words if w in ('prix', 'travaux', 'construction')]
    voc = set(kept)
    print(f"{len(kept)} words kept ({len(voc)} different word forms)")
    fig = plt.figure(figsize = (10,4))
    plt.gcf().subplots_adjust(bottom=0.15) # to avoid x-ticks cut-off
    fdist = nltk.FreqDist(kept)
    print(fdist.most_common(50))
    fdist.plot(50, cumulative=True)
    print(fdist.hapaxes())
    p = 'first50frequency'
    output_path = os.path.join('/Volumes/Extreme SSD/Temp/TPTraitAuto/data/plots/',str(p)+'.png')
    fig.savefig(output_path, bbox_inches = "tight")
#    long_words = [w for w in voc if len(w) > 15]
#   print(sorted(long_words))
