# Getting Links from website and dumping into csv file 

import os
import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup



# page link :: India 

page_links = []
for i in range(1,101):
  page_link = f"https://www.bbc.com/hindi/topics/ckdxnkz7607t/page/{i}"
  page_links.append(page_link)

def GetArticleLink(page_link):

  templink = []
  articlelinks = []

  data = requests.get(page_link)
  soup = BeautifulSoup(data.content, "html.parser")

  articles = soup.find_all("article", class_ = "qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left") 
  for i in articles:
      try:
        j = i.find(class_ = "gel-3/8@l").find('a')['href']
        templink.append(j)
      except Exception as e:
        pass

  for i in templink:
    articlelinks.append(f"https://www.bbc.com{i}")

  return articlelinks


articlelinks = []

for i in page_links:
  linklist = GetArticleLink(i)
  articlelinks.extend(linklist)

df1 = pd.DataFrame(articlelinks, columns=['articlelinks'])


# Getting Links [विज्ञान-टेक्नॉलॉजी]

page_links1 = []
for i in range(1,101):
  page_link = f"https://www.bbc.com/hindi/topics/c2lej0594knt/page/{i}"
  page_links1.append(page_link)

articlelinks1 = []

for i in page_links1:
  linklist = GetArticleLink(i)
  articlelinks1.extend(linklist)

df2 = pd.DataFrame(articlelinks1, columns=['articlelinks'])

# Getting Links [मनोरंजन]

page_links2 = []
for i in range(1,101):
  page_link = f"https://www.bbc.com/hindi/topics/c06gq3n0pp7t/page/{i}"
  page_links2.append(page_link)

articlelinks2 = []

for i in page_links2:
  linklist = GetArticleLink(i)
  articlelinks2.extend(linklist)

df3 = pd.DataFrame(articlelinks2, columns=['articlelinks'])

# Getting Links [खेल]

page_links3 = []
for i in range(1,101):
  page_link = f"https://www.bbc.com/hindi/topics/cwr9j8g1kj9t/page/{i}"
  page_links3.append(page_link)

articlelinks3 = []

for i in page_links3:
  linklist = GetArticleLink(i)
  articlelinks3.extend(linklist)

df4 = pd.DataFrame(articlelinks3, columns=['articlelinks'])

# Getting Links [विदेश]

page_links4 = []
for i in range(1,101):
  page_link = f"https://www.bbc.com/hindi/topics/c9wpm0en87xt/page/{i}"
  page_links4.append(page_link)

articlelinks4 = []

for i in page_links4:
  linklist = GetArticleLink(i)
  articlelinks4.extend(linklist)

df5 = pd.DataFrame(articlelinks4, columns=['articlelinks'])


DF = pd.concat([df1, df2, df3, df4, df5])
DF.reset_index(inplace=True, drop=True)

DF.drop_duplicates(keep='first', inplace=True)
DF.reset_index(inplace=True, drop=True)

DF.to_csv("BBCLinks.csv", header=True, index=False)


# Scrapping & Clearning 

links = "BBCLinks.csv"

linkdf = pd.read_csv(links)

for i, link in enumerate(linkdf['articlelinks']):
  if link.split("/")[4] == "live":
    linkdf.drop(i, axis=0, inplace=True)

linkdf.reset_index(inplace=True, drop=True)

data = requests.get("https://www.bbc.com/hindi/india-61275710")
soup = BeautifulSoup(data.content, "html.parser")

