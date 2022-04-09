import streamlit as st
from PIL import Image
from io import BytesIO
import requests

# import os
# os.system("pip install katonic-1.0-py3-none-any.whl")

import katonic
from katonic.ml.client import MLClient

from joblib import load
import pickle
import joblib

response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))
st.set_page_config(page_title='Movie Genre Prediction',
                   page_icon=im,
                   layout='wide',
                   initial_sidebar_state='auto')
st.title("Movie Genre Prediction with Overview.")
st.image("bloody-mary-genres-big.jpg")
overview = st.text_input("Enter the Overview of a movie.")
predict = st.button("Predict")


def remove_punctuation(input_string):
    input_string = input_string.replace(',', '')
    cleaned_string = input_string.replace('.', '')
    return cleaned_string


Genres_dict = {28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary', 18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History',
               27: 'Horror', 10402: 'Music', 9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller', 10752: 'War', 37: 'Western'}
genre_list = sorted(list(Genres_dict.keys()))

if predict:
    content = []
    overview = overview.replace(',', '')
    overview = overview.replace('.', '')
    content.append(overview)

    vectorize = load("CountVectorizer.joblib")
    X = vectorize.transform(content)

    transformer = load("TFIDF_transformer.joblib")
    X = transformer.transform(X)

    model_ml = joblib.load("best_model.joblib")

    predsnb = model_ml.predict(X)
    infer_preds = []
    pred_genres = []
    movie_label_scores = predsnb[0]
    for j in range(len(movie_label_scores)):
        if movie_label_scores[j] != 0:
            genre = Genres_dict[genre_list[j]]
            pred_genres.append(genre)
            if pred_genres not in infer_preds:
                infer_preds.append(pred_genres)
    predicted_genres = ", ".join(infer_preds[0])
    st.subheader(f"The Predicted genres are {predicted_genres}.")
