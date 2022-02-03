import requests
from io import BytesIO
from PIL import Image
from base64 import b64decode

import streamlit as st
import easyocr as ocr


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))
st.set_page_config(
    page_title='Image to text (OCR)', 
    page_icon = im, 
    layout = 'centered', 
    initial_sidebar_state = 'auto'
)

hide_streamlit_style = '''
            <style>
            footer {visibility: hidden;}
            </style>
            '''
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.image('logo.png')
st.write('''
# Image to Text (OCR)
This app **Extracts the Text from the given Image.!**
''')

st.write('---')
text = st.text_input('Enter Image URL')

if len(text) > 1:
    if text.startswith('data:'):
        header, encoded = text.split(",", 1)
        text = b64decode(encoded)
        st.subheader('Image')
        st.image(text, width=400)
        reader = ocr.Reader(['en'])
        result = reader.readtext(text)

    else:
        response = requests.get(text, stream=True)
        with Image.open(BytesIO(response.content)) as image:
            st.subheader('Image')
            st.image(image, width=400)
            reader = ocr.Reader(['en'])
            result = reader.readtext(response.content)

    result_text = [text[1] for text in result]
    st.subheader('Extracted Text')
    st.success(' '.join(result_text))
else:
    st.info('Please, Upload an Image to process...')

img = st.file_uploader('Upload Image')

if img is not None:
    reader = ocr.Reader(['en'])
    output_img = reader.readtext(img.getvalue())
    cord = [text[1] for text in output_img]
    st.image(Image.open(img), width=400)
    st.subheader('Extracted Text')
    st.success(' '.join(cord))
