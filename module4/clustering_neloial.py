"""Unsupervised clustering example adapted from https://nlpforhackers.io/recipe-text-clustering/"""

import collections
import os
import string
import sys
import yake

from nltk import word_tokenize
from nltk.corpus import stopwords
from pprint import pprint
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
  
ignored = set(["conseil communal", "conseil général"])

kw_extractor = yake.KeywordExtractor(lan="fr", top=20)

def process_text(text, stem=True):
    """ Tokenize text and remove punctuation """
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)
    return tokens
 
def cluster_texts(files, clusters):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    texts = [open(data_path + f).read() for f in files]
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('french'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
 
    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)
    clustering = collections.defaultdict(list)
 
    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(files[idx])
 
    return clustering
 
if __name__ == "__main__":
    data_path = "/Volumes/Extreme SSD/Temp/TPTraitAuto/data/txt/"
    decade = sys.argv[1] # e.g. 1870 or 1930
    files = [f for f in sorted(os.listdir(data_path)) if f"_{decade[:-1]}" in f]
    print(f"{len(files)} documents to cluster for decade {decade}")
    clusters = cluster_texts(files, 2)

    """pprint(dict(clusters))"""
    for cluster, files in clusters.items():
        print(f'{cluster}: {files}')
        for f in sorted(files):
            text = open(data_path + f).read()
            keywords = kw_extractor.extract_keywords(text)
            kept = []
            for score, kw in keywords:
                words = kw.split()
                if len(words) > 2 and kw not in ignored: # only bigrams and more
                    kept.append(kw)
            print(f"{f} mentions these keywords: {', '.join(kept)}...")
