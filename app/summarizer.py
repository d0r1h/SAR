import re
from extractdata import extract_text
from wordcloudplot import plot_wordcloud
from transformers import  AutoModelForSeq2SeqLM, AutoTokenizer

def summarize(input_, model):
  if input_.split("/")[0] == "https:":
    text = extract_text(input_)
  else:
    text = input_

  if model == "T5":
    checkpoint = "csebuetnlp/mT5_multilingual_XLSum"
  elif model == "BART":
    checkpoint = "ai4bharat/IndicBART"

  WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

  tokenizer = AutoTokenizer.from_pretrained(checkpoint)
  model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)


  input_ids = tokenizer(
                  [WHITESPACE_HANDLER(text)],
                  return_tensors="pt",
                  padding="max_length",
                  truncation=True,
                  max_length=512 )["input_ids"]

  output_ids = model.generate(
                    input_ids=input_ids,
                    max_length=70,
                    min_length=30,
                    no_repeat_ngram_size=2,
                    num_beams=4 )[0]     

  
  summary = tokenizer.decode(
                      output_ids,
                      skip_special_tokens=True,
                      clean_up_tokenization_spaces=False)
                      
  figure = plot_wordcloud(text)
  
  return summary, figure  