import gradio as gr
from summarizer import summarize

description = """
<center>
SAR (सार) in Hindi means summary, It's a tool to summarize Hindi News with SOTA models
</center>
"""
article="<p style='text-align: center'> Created by Pawan Trivedi 2022 | <a href='https://github.com/d0r1h/SAR/'>GitHub</a></p>"

link1 = "https://www.amarujala.com/world/india-providing-dry-ration-packs-to-widows-and-needy-families-in-sri-lanka-ahead-of-eid-ins-gharial-brough-medicines-to-colombo-news-in-hindi"

link2 = "https://www.amarujala.com/lucknow/now-the-government-will-go-to-village-to-buy-wheat-in-up-and-wheat-will-also-be-purchased-from-mobile-purchasing-centers"

link3 = "https://www.amarujala.com/india-news/supreme-court-cannot-give-the-status-of-place-of-namaz-without-evidence-rajasthan-waqf-board-s-petition-challenging-the-high-court-order-dismissed?pageId=1"

with open("Example/File.txt", 'r',  encoding="utf8") as f:
    text = f.read()


interface = gr.Interface(fn = summarize,
                        inputs = [gr.inputs.Textbox(lines=5,
                                                    placeholder="Enter your text...",
                                                    label='News Input'),
                                  gr.inputs.Radio(["T5", "BART"], type="value", label='Model')
                                  ],
                          
                        outputs = [gr.outputs.Textbox(label="Sar"), 
                                   gr.outputs.Image(type="plot", label="WordCloud")],
                         
                        title = "Hindi News Summarizer",
                        examples=[[link1, "BART"], 
                                  [link2, "BART"], 
                                  [link3, "BART"], 
                                  [text, "BART"]],
                            
                        description=description,
                        article = article)

interface.launch(debug=True) 