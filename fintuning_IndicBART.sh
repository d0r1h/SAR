
!git clone https://github.com/huggingface/transformers
!pip install -r transformers/examples/pytorch/summarization/requirements.txt

!python /transformers/examples/pytorch/summarization/run_summarization.py \
    --model_name_or_path ai4bharat/IndicBART \
    --do_train \
    --do_eval \
    --train_file /train1k.csv \   # train data
    --validation_file /test.csv \ # test set 
    --text_column text \
    --summary_column summary \
    --output_dir /XXXXX \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate