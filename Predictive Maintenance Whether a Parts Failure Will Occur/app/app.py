import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects  as go
from sklearn.linear_model import LogisticRegression


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Predictive Maintenance Intelligence App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Predictive Maintenance')
st.sidebar.write('---')

st.write("""
# Predictive Maintenance Intelligence App

This app predicts Whether a **Parts Failure Will Occur**!
""")
st.write('---')

# load data
data_df = pd.read_csv('predictive_maintenance.csv')
data_df['broken_str'] = data_df['broken'].replace(0, 'Not Broken').replace(1, 'Broken')
st.write(data_df.head(20))

data_df['team'] = data_df['team'].replace({'TeamA':1,'TeamB':2,'TeamC':3})
data_df['provider'] = data_df['provider'].replace({'Provider1':1,'Provider2':2,'Provider3':3,'Provider4':4})

# showing fig1
st.subheader('Broken Parts % by Provider')
st.caption('Actual Broken Parts percentage with respect to Provider.')
fig = px.bar(data_df.groupby('provider').agg({'broken': 'sum'})/data_df.groupby('provider').agg({'broken': 'count'}))
fig.update_yaxes(title_text = 'Broken Percentage')
fig.update_xaxes(tickangle = 0, title_text='Provider')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('Average Lifetime of Parts (Days)')
labels = 'Broken', 'Not Broken'
sizes = data_df.groupby('broken_str').agg({'lifetime': 'sum'})/data_df.groupby('broken_str').agg({'lifetime': 'count'})
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes.lifetime.to_list())])
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig3
st.subheader('Broken Parts % by Team')
fig = px.bar(data_df.groupby('team').agg({'broken': 'sum'})/data_df.groupby('team').agg({'broken': 'count'}))
fig.update_yaxes(title_text = 'Broken Percentage')
fig.update_xaxes(tickangle = 0, title_text='Team')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    
    provider = st.sidebar.selectbox('Provider',['Provider4','Provider3','Provider2','Provider1'])
    team = st.sidebar.selectbox('Team',['TeamA','TeamB','TeamC'])
    moistureInd = st.sidebar.slider('Moisture Indicator', 0.0, 200.0, 43.0)
    pressureInd = st.sidebar.slider('Pressure Indicator', 0.0, 200.0, 64.0)
    temperatureInd= st.sidebar.slider('Temperature Indicator', 0.0, 200.0, 98.0)
    lifetime = st.sidebar.slider('Lifetime',0, 100, 70)

    data = {
      'provider': provider,
      'team': team,
      'moistureInd': moistureInd,
      'pressureInd': pressureInd,
      'temperatureInd': temperatureInd,
      'lifetime': lifetime,
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

data_df = data_df.drop(['broken_str'], axis=1)

X = data_df.drop(['broken'], axis=1)
y = data_df['broken']

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'finalized_model.sav'
if agree:
    # Build Regression Model
    model = LogisticRegression() 
    model.fit(X, y)
    # save the model to disk
    pickle.dump(model, open(filename, 'wb'))
else:
    # load the model from disk
    model = pickle.load(open(filename, 'rb'))

df = user_input_features()
df['team'] = df['team'].replace({'TeamA':1,'TeamB':2,'TeamC':3})
df['provider'] = df['provider'].replace({'Provider1':1,'Provider2':2,'Provider3':3,'Provider4':4})

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Predictive Maintenance Predictions')
    label = 'Need Maintenance' if prediction > 0.5 else 'No Maintenance Needed'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')
