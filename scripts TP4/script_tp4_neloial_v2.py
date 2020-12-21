"""Analyse frequency distribution of words"""

import nltk
import os
import matplotlib.pyplot as plt
import numpy as np
import sys
from nltk.corpus import stopwords
from collections import defaultdict
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout", 
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu"]
sw = set(sw)
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
# limit = 10**8

data_path = "/Volumes/Extreme SSD/Temp/TPTraitAuto/data/txt2/"
files = os.listdir(data_path)
covered_years = set()
dic = defaultdict(int)


for f in sorted(files):
       if "_" in f:
              elems = f.split("_")
              city = elems[0]
              year = elems[1]
              tome = elems[3]
              part = elems[5]
              covered_years.add(year)
              decade = year[:3] + "0s"
              dic[decade] += 1
       else:
              print(f"Anomalous file: {f}")
       with open(data_path + f, encoding='latin-1') as fil:
              text = fil.read()
              words = nltk.Text(nltk.word_tokenize(text))
              match = words.concordance_list('prix', width=300, lines=100)
              match_lines = "\n".join([cl.line for cl in match])
              #print(f"{f} contains these mentions of price:")
              #print(match)
              output_file = 'sent_prix' + '_' + city + '_' + year + '_' + tome + '_' + part
              output_path = os.path.join('/Volumes/Extreme SSD/Temp/TPTraitAuto/data/sentiment_raw/', output_file)
              with open(output_path, 'w') as fil2:
                     fil2.write(match_lines)
              for input_text in match_lines:
                blob = tb(input_text)
                pola, subj = blob.sentiment
                perc = f"{100*abs(pola):.0f}"
                if pola > 0:
                        sent = f"{perc}% positive"
                elif pola < 0:
                        sent = f"{perc}% negative"
                else:
                        sent = "neutral"
                if subj > 0:
                        fact = f"{100*subj:.0f}% subjective"
                else:
                        fact = "perfectly objective"
                print(f"This text is {sent} and {fact}.")
                sentim = []
                sentim.append(f"This text is {sent} and {fact}.")
                sentim_lines = "\n".join([cl for cl in sentim])
                output_file2 = 'sentim_resultprix' + '_' + city + '_' + year + '_' + tome + '_' + part
                output_path2 = os.path.join('/Volumes/Extreme SSD/Temp/TPTraitAuto/data/sentiment_analysed/', output_file2)
                with open(output_path2, 'w') as fil3:
                     fil3.write(sentim_lines)

# make graph of frequency of the word prix per year 

       with open(data_path + f, encoding='latin-1') as fil:
              text = fil.read()
              words = nltk.wordpunct_tokenize(text)
              print(f"{len(words)} words found")
              kept = [w.lower() for w in words if w in ('prix', 'travaux', 'construction')]
              voc = set(kept)
              print(f"{len(kept)} words kept ({len(voc)} different word forms)")
              fig = plt.figure(figsize = (10,4))
              plt.gcf().subplots_adjust(bottom=0.15) # to avoid x-ticks cut-off
              fdist = nltk.FreqDist(kept)
              print(fdist.most_common(50))
              fdist.plot(3, cumulative=False)
              #fdist.plot(50, cumulative=True)
              print(fdist.hapaxes())
              p = 'plot_' + city + '_' + year + '_' + tome + '_' + part
              output_path = os.path.join('/Volumes/Extreme SSD/Temp/TPTraitAuto/data/plots/',str(p)+'.png')
              fig.savefig(output_path, bbox_inches = "tight")
