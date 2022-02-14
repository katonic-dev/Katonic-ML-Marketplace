import requests
from io import BytesIO
from PIL import Image
from textblob import TextBlob

import streamlit as st


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Sentiment Analyzer App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

hide_streamlit_style = '''
            <style>
            footer {visibility: hidden;}
            </style>
            '''
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

col1, col2 = st.columns(2)
with col1: 
	st.image('logo.png', width=200)
with col2:
	st.write("")

st.title("Sentiment Analyzer App")
st.write("This App analyze **the sentiment of the user, whether it is Some What Positive, Positive, Very Positive, Some What Negative, Negative, Very Negative or Neutral!**")
st.write('---')

st.subheader("Example: ")
st.write("""For the given review like **Product was excellent and works better than the earlier one and Boy was it cheaper!** the predicted sentiment can be **Some What Positive, Positive, Very Positive, Some What Negative, Negative, Very Negative or Neutral.**""")
st.write('---')

st.subheader("Time to Analyze the Text")
with st.form(key='nlpForm'):
	raw_text = st.text_area("Enter Text Here")
	submit_button = st.form_submit_button(label='Analyze')

# layout
col1, col2 = st.columns(2)
if submit_button:

	with col1:
		sentiment = TextBlob(raw_text).sentiment
		blob = TextBlob(raw_text)
		result = blob.sentiment.polarity
		st.subheader("Result")

		if (0.2 > sentiment.polarity > 0.2):
			st.success("**Sentiment :: Some What Positive : 😀** ")
		elif (-0.2 < sentiment.polarity < -0.2):
			st.error("**Sentiment :: Some What Negative : 😤** ")
		elif (-0.1 < sentiment.polarity < 0.1):
			st.warning("**Sentiment :: Neutral  😐** ")
		elif (0.6 > sentiment.polarity >= 0.2):
			st.success("**Sentiment :: Positive : 😊** ")
		elif (-0.6 < sentiment.polarity <= -0.2):
			st.error("**Sentiment :: Negative : 😠** ")
		elif (sentiment.polarity  >= 0.6):
			st.success("**Sentiment :: Very Positive : 😍** ")
		elif (sentiment.polarity <= -0.6):
			st.error("**Sentiment :: Very Negative : 😡** ")
		else:
			pass
