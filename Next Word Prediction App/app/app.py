from transformers import BertTokenizer, BertForMaskedLM
import streamlit as st
from io import BytesIO
from PIL import Image
import torch
import string
import os
import sys
import time
import requests

response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Next word Prediction App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.write('---')

st.markdown('# **Next word Prediction App **')
st.write("""
This app **predicts the next word for the given input to make more personalized sentences.!**
""")
st.write("""
For the given text like **"how many people"** the next suggested words can be **live, visit, die etc...** and more according to the 
number of words you want.
""")
st.write('---')


#use joblib to fast your function

def decode(tokenizer, pred_idx, top_clean):
  ignore_tokens = string.punctuation + '[PAD]'
  tokens = []
  for w in pred_idx:
    token = ''.join(tokenizer.decode(w).split())
    if token not in ignore_tokens:
      tokens.append(token.replace('##', ''))
  return '\n'.join(tokens[:top_clean])

def encode(tokenizer, text_sentence, add_special_tokens=True):
  text_sentence = text_sentence.replace('<mask>', tokenizer.mask_token)
    # if <mask> is the last token, append a "." so that models dont predict punctuation.
  if tokenizer.mask_token == text_sentence.split()[-1]:
    text_sentence += ' .'

    input_ids = torch.tensor([tokenizer.encode(text_sentence, add_special_tokens=add_special_tokens)])
    mask_idx = torch.where(input_ids == tokenizer.mask_token_id)[1].tolist()[0]
  return input_ids, mask_idx

def get_all_predictions(text_sentence, top_clean=5):
    # ========================= BERT =================================
  input_ids, mask_idx = encode(bert_tokenizer, text_sentence)
  with torch.no_grad():
    predict = bert_model(input_ids)[0]
  bert = decode(bert_tokenizer, predict[0, mask_idx, :].topk(top_k).indices.tolist(), top_clean)
  return {'bert': bert}

def get_prediction_eos(input_text):
  try:
    input_text += ' <mask>'
    res = get_all_predictions(input_text, top_clean=int(top_k))
    return res
  except Exception as error:
    pass

st.sidebar.subheader('Next Word ')
top_k = st.sidebar.slider('Select How many words do you need', 1, 25, 1) #some times it is possible to have less words
input_text = st.text_area("Enter your text here: ")

if st.sidebar.button('Predict'): 
    #Bert tokenizer that tokenizes the text
 bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    # using pretrained model
 bert_model = BertForMaskedLM.from_pretrained('bert-base-uncased').eval()

    #click outside box of input text to get result
 res = get_prediction_eos(input_text)

 answer = []
 
 for i in res['bert'].split("\n"):
  answer.append(i)

 answer_as_string = "    ".join(answer)
 st.text_area("Suggested Words", answer_as_string, key="predicted_list") 

else:
    st.warning("Click on Prediction")
st.write('---')  

hide_streamlit_style = '''
<style>
footer {visibility: hidden;}
</style>
'''
st.markdown(hide_streamlit_style, unsafe_allow_html=True)