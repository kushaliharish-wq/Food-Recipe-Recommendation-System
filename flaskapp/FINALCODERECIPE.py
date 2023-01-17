#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from IPython import display
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

ds = pd.read_csv('C:/Users/win10/Desktop/flaskapp/templates/dataset.csv',encoding= 'unicode_escape')
with open('C:/Users/win10/Desktop/flaskapp/templates/dataset.csv', 'rb') as f:
  text = f.read()

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 5), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(ds['name'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix) 
results = {}
for idx, row in ds.iterrows():
   similar_indices = cosine_similarities[idx].argsort()[:-100:-1] 
   similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices] 
   results[row['id']] = similar_items[1:]

def match_name(name):
    return ds.loc[ds['name'] == name]['id'].tolist()[0]

def item(id):  
  return ds.loc[ds['id'] == id]['name'].tolist()[0] 

def match_ing(id):
 return ds.loc[ds['id'] == id]['ingredients'].tolist()[0]

def match_recipe(id):
 return ds.loc[ds['id'] == id]['recipe'].tolist()[0]

def match_link(id):
  return ds.loc[ds['id'] == id]['links'].tolist()[0]


def recommend(id, num=5):
    recs = results[id][:num]
    name_fin = []
    ing_list = []
    rec_list = []
    link_list = []
    for rec in recs:
        get_name = item(rec[1]) + match_ing(rec[1]) + match_recipe(rec[1]) + match_link(rec[1])
        name_fin.append(item(rec[1]))
        ing_list.append(match_ing(rec[1]))
        rec_list.append(match_recipe(rec[1]))
        link_list.append(match_link(rec[1]))
        #print("Hi.... {}" .format(get_name))
    return name_fin, ing_list, rec_list, link_list


