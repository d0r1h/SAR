import os
import re
import pandas as pd

data_path = "/SAR/hindi_news/datasets/"
os.listdir(data_path)

data = pd.read_json(data_path + 'HindiSummaries1.json', orient ='split', compression = 'infer')

noise1 = re.compile(r"[([].*?[\)\]]\s+") # वर्ल्ड कप 2019 (World Cup 2019)  --> वर्ल्ड कप 2019 
noise2 = re.compile(r"\{.*?\}")  # { googletag.display{ googletag.display(div-gpt-ad-1517823702248-0); });} }
noise3 = re.compile(r"[a-zA-Z]")
noise4 = re.compile(r"[\{()#@:%,_;}\]]")
noise5 = re.compile(r'[\?\]]')

def clean(doc_):

  doc = re.sub('\n', ' ', doc_)
  doc = re.sub('\r', ' ', doc)
  doc = re.sub('\u200d', ' ', doc)
  doc = re.sub('\xa0', ' ', doc)
  doc = re.sub(noise1, ' ', doc)
  doc = re.sub(noise2, ' ', doc)
  doc = re.sub(noise3, ' ', doc)
  doc = re.sub(noise4, ' ', doc)
  doc = re.sub(noise5, ' ', doc)
  doc = re.sub('[\']', ' ', doc)
  doc = re.sub('-', ' ', doc)
  doc = re.sub('❤️', ' ', doc)
  doc = re.sub(' +', ' ', doc)
  
  return doc


data['clean_text'] = data['text'].map(lambda x: clean(x))
data['clean_summaries'] = data['summarie'].map(lambda x: clean(x))
data['clean_titles'] = data['title'].map(lambda x: clean(x))

data[['clean_text',	'clean_summaries',	'clean_titles']].to_json(data_path + 'HindiSummariesClean1.json', 
                                                                 orient = 'split', 
                                                                 compression = 'infer')


