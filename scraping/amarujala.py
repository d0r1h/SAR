# This crawler ran from Apr 29 2022

import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

html_element = re.compile(r'<.*?>')
englishreg = re.compile(r'[A-Za-z-]')

# Links 
news1 = "https://www.amarujala.com/world"
news2 = "https://www.amarujala.com/india-news"
news3 = "https://www.amarujala.com/uttar-pradesh"
news4 = "https://www.amarujala.com/haryana"
news5 = "https://www.amarujala.com/punjab"
news6 = "https://www.amarujala.com/jammu-and-kashmir"
news7 = "https://www.amarujala.com/himachal-pradesh"
news8 = "https://www.amarujala.com/uttarakhand"
news9 = "https://www.amarujala.com/rajasthan"
news10 = "https://www.amarujala.com/bihar"
news11 = "https://www.amarujala.com/chhattisgarh" 
news12 = "https://www.amarujala.com/jharkhand"
news13 = "https://www.amarujala.com/madhya-pradesh"
news14 = "https://www.amarujala.com/delhi"
news15 = "https://www.amarujala.com/business"
news16 = "https://www.amarujala.com/cricket"

news = [news1, news2, news3, news4, news5, news6, news7, news8, news9, news10, news11, news12,news13, news14, news15, news16]

def get_links(url):

  data = requests.get(url)
  soup = BeautifulSoup(data.content, "html.parser")
  links = [i.find_all('a')[-1].attrs.get('href') for i in soup.find_all('div', class_ = "image_description")]
  for i in links:
    if i.split('/')[1] != url.split('/')[-1]:
      links.remove(i)
  FinalLinks = ["https://www.amarujala.com" + i for i in links]
  return FinalLinks

links = []
for i in news:
  links.extend(get_links(i))


"""
url example to clean 

https://www.amarujala.com/photo-gallery/dehradun/women-congress-workers-protest-against-cooperative-bank-recruitment-scam-case-see-photos',
https://www.amarujala.com/video/haryana/three-killed-in-road-accident-in-siwani-mandi-of-hisar',
https://www.amarujala.com/podcast/haryana/haryana-ki-awaaz/jash-murder-case-in-karnal-father-ramphal-will-not-return-from-america',
"""

noise = ["podcast", "video", "photo-gallery", "www.amarujala.comhttps:"]

for i in links:
  if i.split('/')[3] in noise:
    links.remove(i)

linkdf = pd.DataFrame(links, columns=['links'])

for i in linkdf['links']:
  print(i)

# Getting Data

news_link = linkdf

news_link.drop(17, axis=0, inplace=True)

titles, summaries, text = [], [], []

for k ,i in enumerate(news_link['links']):

  data = requests.get(i)
  soup = BeautifulSoup(data.content, "html.parser")

  try:
    title = soup.find("title").text
    title = ' '.join([word for word in title.split(' ') if not word.isalpha()])
  except Exception as e:
    title = np.NaN

  try:
    sar = soup.find(class_ = "khas-batei ul_styling")
    sar = sar.text
  except Exception as e:
    sar = np.NaN 

  try:
    vistaar = soup.find(class_ = "article-desc ul_styling")
    vistaar = vistaar.text
  except Exception as e:
    vistaar = np.NaN

  titles.append(title)
  summaries.append(sar)
  text.append(vistaar)

  print(k, i)

print(len(titles), len(summaries), len(text))

df = pd.DataFrame(list(zip(titles, summaries, text)), columns =['titles', 'summaries','text'])

df['summaries'] = df['summaries'].apply(lambda x: str(x).replace("\nसार \n", ""))
df['text'] = df['text'].apply(lambda x: str(x).replace("विस्तार ", ""))
df['text'] = df['text'].apply(lambda x: str(x).replace("विज्ञापन", ""))
df['text'] = df['text'].apply(lambda x: str(x).replace("\n", ""))


df.to_json("amarujala_sum_valid1.json", orient ='split', compression = 'infer')