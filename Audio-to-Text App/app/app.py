import os
import requests
from PIL import Image
from io import BytesIO
from zipfile import ZipFile
import streamlit as st
from pytube import YouTube


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Audio to Text App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

# st.sidebar.image('logo.png')
st.sidebar.title('Audio to Text App')
st.sidebar.write('---')

st.markdown('# **Audio-to-Text**')
st.write("""
This app **Extracts the Text from the given video!**
""")
bar = st.progress(0)
st.write('---')

# 1. Retrieving audio file from YouTube video
def get_yt(URL):
    video = YouTube(URL)
    yt = video.streams.filter(only_audio=True).first()
    yt.download()
    bar.progress(10)

# 2. Upload YouTube audio file to AssemblyAI
def transcribe_yt():
    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        if file.endswith('.mp4'):
            mp4_file = os.path.join(current_dir, file)
    
    filename = mp4_file
    bar.progress(20)

    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    headers = {'authorization': api}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=read_file(filename))
    audio_url = response.json()['upload_url']
    bar.progress(30)

    # 3. Transcribe uploaded audio file
    endpoint = 'https://api.assemblyai.com/v2/transcript'

    json = {
    'audio_url': audio_url
    }

    headers = {
        'authorization': api,
        'content-type': 'application/json'
    }

    transcript_input_response = requests.post(endpoint, json=json, headers=headers)

    bar.progress(40)

    # 4. Extract transcript ID
    transcript_id = transcript_input_response.json()['id']
    bar.progress(50)

    # 5. Retrieve transcription results
    endpoint = f'https://api.assemblyai.com/v2/transcript/{transcript_id}'
    headers = {
        'authorization': api,
    }
    transcript_output_response = requests.get(endpoint, headers=headers)

    bar.progress(60)

    # 6. Check if transcription is complete
    from time import sleep

    while transcript_output_response.json()['status'] != 'completed':
        sleep(5)
        st.warning('Transcription is processing ...')
        transcript_output_response = requests.get(endpoint, headers=headers)

    if transcript_output_response.json()['status'] == 'completed':
        st.success('Transcription is processed!')

    bar.progress(100)

    # 7. Print transcribed text
    st.header('Output')
    st.success(transcript_output_response.json()['text'])

    # 8. Save transcribed text to file

    # Save as TXT file
    yt_txt = open('yt.txt', 'w')
    yt_txt.write(transcript_output_response.json()['text'])
    yt_txt.close()

    # Save as SRT file
    srt_endpoint = endpoint + '/srt'
    srt_response = requests.get(srt_endpoint, headers=headers)
    with open('yt.srt', 'w') as _file:
        _file.write(srt_response.text)
    
    zip_file = ZipFile('transcription.zip', 'w')
    zip_file.write('yt.txt')
    zip_file.write('yt.srt')
    zip_file.close()
#####

# Sidebar
st.sidebar.header('Input parameter')


with st.sidebar.form(key='my_form'):
 URL = st.text_input('Enter URL of YouTube video:')
 api = st.text_input('Enter API key')
 link = 'https://www.assemblyai.com/'
 st.markdown(link, unsafe_allow_html=True)
 st.write('Sign up for free and get your API key')
 submit_button = st.form_submit_button(label='Go')

# Run custom functions if URL is entered 
if submit_button:
    get_yt(URL)
    transcribe_yt()

    with open('transcription.zip', 'rb') as zip_download:
        btn = st.download_button(
            label='Download ZIP',
            data=zip_download,
            file_name='transcription.zip',
            mime='application/zip'
        )


hide_streamlit_style = '''
            <style>
            footer {visibility: hidden;}
            </style>
            '''
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
