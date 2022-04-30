import re
import requests
from bs4 import BeautifulSoup


noise1 = re.compile(r"[([].*?[\)\]]\s+") # वर्ल्ड कप 2019 (World Cup 2019)  --> वर्ल्ड कप 2019 
noise2 = re.compile(r"\{.*?\}")  # { googletag.display{ googletag.display(div-gpt-ad-1517823702248-0); });} }
noise3 = re.compile(r"[a-zA-Z]")
noise4 = re.compile(r"[\{()#@:%,_;&!=}\]]")
noise5 = re.compile(r'[\?\]]')


def extract_text(url):
  
  data = requests.get(url)
  soup = BeautifulSoup(data.content, "html.parser")
  
  try:
    vistaar = soup.find(class_ = "article-desc ul_styling")
    vistaar = vistaar.text
  except Exception as e:
    print(f"Not able to fetch text {e}")

  vistaar = vistaar.replace("विस्तार ", ' ')
  vistaar = vistaar.replace("विज्ञापन", ' ')
  vistaar = vistaar.replace("\n", ' ')
  vistaar = re.sub('\xa0', ' ', vistaar)
  vistaar = re.sub(noise2, ' ', vistaar)
  vistaar = re.sub(noise3, ' ', vistaar)
  vistaar = re.sub(noise4, ' ', vistaar)
  vistaar = re.sub(' +', ' ', vistaar)

  return vistaar