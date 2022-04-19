import gradio as gr
from summarize import Summarizer

interface = gr.Interface(fn = Summarizer,
                        inputs = [gr.inputs.Textbox(lines=2, 
                                                    placeholder="Enter your link...",
                                                    label='YouTube Video Link'),
                                  gr.inputs.Radio(["mT5", "BART", "Pegasus"], type="value", label='Model')],
                        outputs = [gr.outputs.Textbox(
                                                      label="Summary")],
                         
                        title = "Youtube Summarizer",
                        examples = [['https://www.youtube.com/watch?v=A4OmtyaBHFE', 'mT5'],
                                   ['https://www.youtube.com/watch?v=cU6xVZfkcgo', 'mT5']],
                        enable_queue=True)

interface.launch(debug=True) 