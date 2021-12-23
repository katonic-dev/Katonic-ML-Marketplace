from datetime import datetime, time
import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import numpy as np

import streamlit as st
import plotly.express as px
import plotly.graph_objects  as go

from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import GradientBoostingRegressor


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='MTTR Predictor App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('MTTR Predictor')
st.sidebar.write('---')

st.write("""
# MTTR (Mean Time to Resolution) Predictor App

This app predicts **The Time taken by a Service Agent to Solve a Specific Ticket or an Incident Request**.
""")
st.write('---')

# load data
data_path = 'mttr_predictor.csv'
data_df = pd.read_csv(data_path, parse_dates=['Request Submitted Date and Time','Request Resolved Date and Time'])
st.write(data_df.head(20))

data_df = data_df[data_df['Request Status']=='Closed'].reset_index(drop=True)
data_df['mttr'] = data_df['Request Resolved Date and Time']-data_df['Request Submitted Date and Time']
data_df['mttr_day'] = data_df['mttr'].apply(lambda x: x.total_seconds()/(3600*24))
data_df['mttr'] = data_df['mttr'].apply(lambda x: x.total_seconds()/60)

# showing fig1
st.subheader('Average Time Taken to Resolve a Particular Ticket')
fig = px.bar(data_df.groupby('Request Category').agg({'mttr_day': 'sum'})/data_df.groupby('Request Category').agg({'mttr_day': 'count'}))
fig.update_yaxes(title_text = 'Average Time Taken (in Days) to Resolve')
fig.update_xaxes(tickangle = -45, title_text='Type of Request')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# # showing fig2
st.subheader('Time Taken to Resolve by Priority')
labels = '3-Low', '2-Medium', '1-High'
sizes = [data_df['Request Priority'][data_df['Request Priority']=='3-Low'].count(), data_df['Request Priority'][data_df['Request Priority']=='2-Medium'].count(), data_df['Request Priority'][data_df['Request Priority']=='1-High'].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.1, 0, 0])])
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

def user_input_features():
    
    request_submitted_date = st.sidebar.date_input('The date when the Request was Submitted', datetime(2016, 4, 1))
    request_submitted_time = st.sidebar.time_input('The time when the Request was Submitted', time(8, 10))
    request_submitted_date_and_time = datetime.combine(request_submitted_date, request_submitted_time)
    request_priority = st.sidebar.selectbox('Priority of the Request', options=['3-Low', '2-Medium', '1-High'])
    request_category = st.sidebar.selectbox('Type of Request', options=list(data_df['Request Category'].unique()))
    request_status = st.sidebar.selectbox('Status of the Request', options=['Open'])
    
    data = {
      'Request Submitted Date and Time': request_submitted_date_and_time,
      'Request Priority': request_priority,
      'Request Category': request_category,
      'Request Status': request_status,
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

data_df['Request Priority'] = data_df['Request Priority'].apply(lambda x: x.split('-')[0])
data_df['mttr'][data_df['mttr']<0] = 0
data_df['mttr'] = np.log(data_df['mttr']+1)

data_df = data_df.drop(columns=['Request ID', 'Request Resolved By', 'Request Submitted Date and Time', 'Request Resolved Date and Time', 'Request Status', 'mttr_day'], axis=1)

oe = OrdinalEncoder(
    handle_unknown='use_encoded_value',
    unknown_value=-99
)
data_df['Request Category'] = oe.fit_transform(data_df['Request Category'].values.reshape(-1,1))
st.write(data_df.head())

X = data_df.drop(['mttr'], axis=1)
y = data_df['mttr']

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'finalized_model.sav'
if agree:
    # Build Regression Model
    model = GradientBoostingRegressor(
        max_depth=4,
        max_features='sqrt', 
        min_samples_leaf=1,
        min_samples_split=12, 
        n_estimators=200,
        random_state = 42,
        learning_rate=0.16
    )
    model.fit(X, y)
    # save the model to disk
    pickle.dump(model, open(filename, 'wb'))
else:
    # load the model from disk
    model = pickle.load(open(filename, 'rb'))

df = user_input_features()
df['Request Priority'] = df['Request Priority'].apply(lambda x: x.split('-')[0])
df['Request Category'] = oe.fit_transform(df['Request Category'].values.reshape(-1,1))

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

df = df[['Request Priority','Request Category']]

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Mean Time to Resolution Predictions')
    st.write(f'Mean Time To Resolution: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')
