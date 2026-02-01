import re
import torch
import pandas as pd 
from rouge import Rouge
from transformers import  AutoModelForSeq2SeqLM, AutoTokenizer

df = pd.read_json("data50k.json", orient ='split', compression = 'infer')

df1 = df.sample(n=2000)

df1.reset_index(drop=True, inplace=True)

print(df1.shape)

# IndicBART 

tokenizer_bart = AutoTokenizer.from_pretrained("ai4bharat/IndicBART", do_lower_case=False, use_fast=False, keep_accents=True)
model_bart = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/IndicBART")

bos_id = tokenizer_bart._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer_bart._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer_bart._convert_token_to_id_with_added_voc("<pad>")

text1 = df1['text'][0].replace("\xa0", '')

inp = tokenizer_bart(text1, add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

model_output = model_bart.generate(inp, use_cache=True, 
                            num_beams=4, 
                            max_length=70, 
                            min_length=30, 
                            early_stopping=True, 
                            pad_token_id=pad_id,
                            bos_token_id=bos_id, 
                            eos_token_id=eos_id, 
                            decoder_start_token_id=tokenizer_bart._convert_token_to_id_with_added_voc("<2en>"))

decoded_output = tokenizer_bart.decode(model_output[0], 
                                skip_special_tokens=True, 
                                clean_up_tokenization_spaces=False)

rouge = Rouge()
score = rouge.get_scores(decoded_output, df1['summary'][0])

print(pd.DataFrame(score[0]).set_index([['recall','precision','f-measure']]))


# mT5 multilingual XLSum

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

text1 = df1['text'][0].replace("\xa0", '')

model_name = "csebuetnlp/mT5_multilingual_XLSum"

tokenizer_t5 = AutoTokenizer.from_pretrained(model_name)
model_t5 = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_ids = tokenizer_t5(
          [WHITESPACE_HANDLER(text1)],
          return_tensors="pt",
          padding="max_length",
          truncation=True,
          max_length=512
          
)["input_ids"]

output_ids = model_t5.generate(
                    input_ids=input_ids,
                    max_length=70,
                    min_length=30,
                    no_repeat_ngram_size=2,
                    num_beams=4
)

summary = tokenizer_t5.decode(
                      output_ids[0],
                      skip_special_tokens=True,
                      clean_up_tokenization_spaces=False
)


score_mt5 = rouge.get_scores(summary, df1['summary'][0])
print(pd.DataFrame(score_mt5[0]).set_index([['recall','precision','f-measure']]))


print(f"Actual : {df1['summary'][0]}")
print(f"IndicBart : {summary}")
print(f"mt5 : {decoded_output}")