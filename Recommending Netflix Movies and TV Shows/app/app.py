import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects  as go
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Netflix Movie Recommendation', 
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

st.sidebar.image('logo.png')
st.sidebar.title('Netflix Movie Recommendation')
st.sidebar.write('---')

st.write('''
# Netflix Movie Recommendation App

This app **Recommends Movies to the User based on their Searches (Content)!**
''')
st.write('---')

# Loads the Dataset
data_path = 'netflix_titles.csv'
data_df = pd.read_csv(data_path)
data_df['description'] = data_df['description'].fillna('')
st.write(data_df.head(20))

# showing fig1
st.subheader('Movies vs TV Shows on Netflix')
labels = 'TV Shows', 'Movies'
sizes = [data_df.type[data_df['type']=='TV Show'].count(), data_df.type[data_df['type']=='Movie'].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.1, 0, 0])])
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
fig.update_traces(marker=dict(colors=['darkblue', 'cyan']))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('Which Year most of the movies were Released?')
st.write('> 2018 was the year when most of the movies were released.')
count_df = data_df.groupby(by=['release_year']).size().reset_index(name='counts')
fig = px.bar(data_frame=count_df[-15:], x='release_year', y='counts', color='release_year', barmode='group')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
fig.update_yaxes(title_text = 'No. of Movies Realeased')
fig.update_xaxes(tickangle = 0, title_text='Release Year')
st.plotly_chart(fig, use_container_width=False)

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(data_df['description'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data_df.index, index=data_df['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return data_df['title'].iloc[movie_indices]

data_df2 = data_df.copy()
filledna = data_df2.fillna('')

def clean_data(x):
    return str.lower(x.replace(' ', ''))

features = ['title', 'director', 'cast', 'listed_in', 'description']
filledna = filledna[features]

for feature in features:
    filledna[feature] = filledna[feature].apply(clean_data)

def create_soup(x):
    return x['title']+ ' ' + x['director'] + ' ' + x['cast'] + ' ' +x['listed_in']+' '+ x['description']

filledna['soup'] = filledna.apply(create_soup, axis=1)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(filledna['soup'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix) 

filledna=filledna.reset_index()
indices2 = pd.Series(filledna.index, index=filledna['title'])

def get_recommendations_new(title, cosine_sim=cosine_sim2):
    title=title.replace(' ','').lower()
    idx = indices2[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return data_df2['title'].iloc[movie_indices]

def user_input_features():
    title_list = list(data_df.title.unique())
    return st.sidebar.selectbox('Select or Enter Movie Title', options=title_list)

# Main Panel

Title = user_input_features()

# Print specified input parameters
st.header('Specified Movie Title as Input Parameter')
st.write(f'User Searches for: **{Title}**')
st.write('---')

# Apply Model to Make Prediction
if st.sidebar.button('Recommend'):
    st.header('Top Recommendations: ')
    st.subheader('Recommendations on Single Metric (Movie Description): ')
    st.table(data=get_recommendations(Title))
    st.subheader('Recommendations on Multiple Metric (Title, Director, Cast, Description, Listed In): ')
    st.table(data=get_recommendations_new(Title, cosine_sim2))
else:
    st.warning('Please Click on Recommendation')
st.write('---')
