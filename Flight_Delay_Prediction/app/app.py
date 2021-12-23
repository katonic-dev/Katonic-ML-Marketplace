import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects  as go
from sklearn.ensemble import RandomForestRegressor


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Flight Delay Prediction App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Flight Delay Prediction')
st.sidebar.write('---')

st.write("""
# Flight Delay Prediction App

This app predict **Fligh Delay** due to various parameters!
""")
st.write('---')

# Loads the Dataset
data_path = "flight_delay_prediction.csv"
data_df = pd.read_csv(data_path)
data_df = data_df.drop(['OP_CARRIER_AIRLINE_ID', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID'], axis=1)
st.write(data_df.head(20))

# showing fig1
st.subheader('Percentage Flights Delay due to Departure Delay')
labels = 'Departure Delay', 'On-Time Departure'
sizes = [data_df.DEP_DEL15[data_df['DEP_DEL15']==1].count(), data_df.DEP_DEL15[data_df['DEP_DEL15']==0].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.2, 0, 0])])
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('Distance Covered count vs All parameters')
avg_value_df = data_df.groupby("DISTANCE").mean()
fig = px.bar(data_frame=avg_value_df)
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig3
st.subheader('Percentage Flights Delay in Total Flights')
labels = 'Delayed Flight', 'On-Time Flight'
sizes = [data_df.ARR_DEL15[data_df['ARR_DEL15']==1].count(), data_df.ARR_DEL15[data_df['ARR_DEL15']==0].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.08, 0, 0])])
fig.update_traces(marker=dict(colors=['darkblue', 'cyan']))
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

def user_input_features():

    DAY_OF_MONTH = st.sidebar.slider('Day Of Month', 1, 30, 12)
    DAY_OF_WEEK = st.sidebar.slider('Day Of Week', 1, 7, 3)
    DEP_TIME = st.sidebar.slider('Departure Time', 515, 2343, 1000)
    DEP_DEL15 = st.sidebar.selectbox('Departure Delay', [0, 1])
    ARR_TIME = st.sidebar.slider('Arrival Time', 1, 2358, 200)
    DIVERTED = st.sidebar.selectbox('Diverted', [0, 1])
    DISTANCE = st.sidebar.slider('Distance (KM)', 74, 2447, 2000)

    data = {
        'DAY_OF_MONTH': DAY_OF_MONTH, 
        'DAY_OF_WEEK': DAY_OF_WEEK, 
        'DEP_TIME': DEP_TIME, 
        'DEP_DEL15': DEP_DEL15,
        'ARR_TIME': ARR_TIME, 
        'DIVERTED': DIVERTED, 
        'DISTANCE': DISTANCE
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

X = data_df.drop(['ARR_DEL15'], axis=1)
y = data_df['ARR_DEL15']

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'finalized_model.sav'
if agree:
    # Build Regression Model
    model = RandomForestRegressor()
    model.fit(X, y)
    # save the model to disk
    pickle.dump(model, open(filename, 'wb'))
else:
    # load the model from disk
    model = pickle.load(open(filename, 'rb'))

df = user_input_features()

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Apply Model to Make Prediction
if st.sidebar.button("Prediction"):
    prediction = model.predict(df)

    st.header('Flight Delay Predictions')
    label = "Delay" if prediction > 0.5 else "On Time"
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning("Please Click on Prediction")
st.write('---')
