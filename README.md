<p align="center">
    <br>
    <img src="https://github.com/d0r1h/SAR/blob/main/assets/logo.png" width="300"/>
    <br>
<p>
  
<p align="center">
    <a href="https://huggingface.co/spaces/d0r1h/Hindi_News_Summarizer">
    <img alt="Website" src="https://img.shields.io/website?down_color=red&down_message=offline&up_color=yellow&up_message=online&url=https%3A%2F%2Fhuggingface.co%2Fspaces%2Fd0r1h%2FHindi_News_Summarizer">
    </a>
    <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fd0r1h%2FSAR&count_bg=%2379C83D&title_bg=%23555555&icon=googlenews.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false"/>
    </a>
    <a href="https://twitter.com/intent/tweet?text=Checkout this awesome project for summarizing Hindi text:&url=https%3A%2F%2Fgithub.com%2Fd0r1h%2FSAR%2F">
    <img alt="tweet" src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fd0r1h%2FSAR%2F">
    </a>
  </p>
  
 <h4 align="center">
    <p>State-of-the-art Summarization methods for Hindi in 🤗 </p>
</h4>

<h3 align="center">
    <a href="https://huggingface.co/spaces/d0r1h/Hindi_News_Summarizer"><img src="https://github.com/d0r1h/SAR/blob/main/assets/sar_app.png", width="550"></a>
</h3>

SAR (सार) in Hindi means summary. This repository contains my work on Hindi Text Summarization on news article.  

Access complete dataset on [huggingface](https://huggingface.co/datasets/d0r1h/HindiNewSummaries)

### Notebook:

| Notebook | Colab | Kaggle |
| ------ | ------ | ------ |
| BaseLine | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/d0r1h/SAR/blob/main/notebooks/baseline.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/undersc0re/hindi-text-summarization-baseline) |


### DataSet:

* As of now I've released a sample Dataset of 2k pairs of text and summary which can be accessed at [Link](https://github.com/d0r1h/SAR/tree/main/dataset)


### Models:

* Inference results are on 2k sample data.

|Model | Checkpoint | Rouge-2[f_score] | 
|--- | --- | --- |
|BART | [ai4bharat/IndicBART](https://huggingface.co/ai4bharat/IndicBART) | 21.48 | 
|T5 | [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) | 20.21 | 


### Project Pipeline

<h3 align="center">
    <img src="https://github.com/d0r1h/SAR/blob/main/assets/SAR.png", width="550"></a>
</h3>


### API

You can summarize any Hindi news article in just 5 lines of code

```python
>>> import requests
>>> api_endpoint = "https://hf.space/embed/d0r1h/Hindi_News_Summarizer/+/api/predict/"
>>> news_url = "https://www.amarujala.com/uttar-pradesh/shamli/up-news-heroin-caught-in-shaheen-bagh-of-delhi-is-connection-to-kairana-and-muzaffarnagar?src=tlh\u0026position=3"
>>> r = requests.post(url= api_endpoint, 
                  json = {"data": [ news_url, "BART"]})
>>> r.json()['data'][0]
>>> यूपी शाहीन बाग में 100 करोड़ रुपये कीमत की हेरोइन और अन्य मादक पदार्थ की बरामदगी व उसे लाने अंतर्राष्ट्रीय ड्रग्स तस्करों के गिरोह के तार शामली जिले के कस्बा कैराना और मुजफ्फरनगर से जुड़ रहे हैं। नारकोटिक्स कंट्रोल ब्यूरो एनसीबी दिल्ली की टीम ने गुरुवार को कैलाना से दो लोगों को हिरासत में
```


### Inference Demo:

Application is hosted on 🤗 space and can be accessed at [SAR](https://huggingface.co/spaces/d0r1h/Hindi_News_Summarizer)

### Website Supported

- [x] [Amarujala](https://www.amarujala.com)


#### ToDO

- [ ] Add support for following website
    - [ ] [aajtak](https://www.aajtak.in/)
    - [ ] [ndtv](https://ndtv.in/)  
- [ ] Foramtting Hindi text for wordcloud
