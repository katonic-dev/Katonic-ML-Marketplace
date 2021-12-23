import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
from fbprophet import Prophet


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Retail Sales Forecasting App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Retail Sales Forecasting')
st.sidebar.write('---')

st.write("""
# Retail Sales Forecasting App

Retail Sales forecasting  helps retailers to **Predict Future Sales and thereby Optimize their Inventory, Logistics, Warehouse Management, Production Planning, Personnel Allocation, etc.** based on historic data.
""")
st.write('---')

# Loads Dataset
data_path = 'retail_sales_time_series.csv'
data_df = pd.read_csv(data_path, index_col = [0])
data_df = data_df.T.copy().reset_index().rename(mapper={'index':'date','product_1':'retail_sales'}, axis=1)
st.write(data_df.head(20))
data_df = data_df.rename(mapper={'date':'ds','retail_sales':'y'}, axis=1)

# showing fig1
st.header('Date vs Monthly Sales')
fig = px.line(data_df, x='ds', y='y')
fig.update_yaxes(title_text = 'Monthly Sales')
fig.update_xaxes(title_text='Date')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    
    return st.sidebar.slider('Period', 1, 40, 30)

# Main Panel

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'finalized_model.sav'
if agree:

    # Build Regression Model
    model = Prophet()
    model.fit(data_df)

    # save the model to disk
    pickle.dump(model, open(filename, 'wb'))
else:
    # load the model from disk
    model = pickle.load(open(filename, 'rb'))

period = user_input_features()

# Print specified input parameters
st.header('Specified Input parameters')
st.write(f'Period: **{period}**')
st.write('---')

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    future = model.make_future_dataframe(periods=period)
    forecast = model.predict(future)
    st.header('Retail Sales Forecast')
    st.write('Forecasting Scores:')
    st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
    st.write('---')

    st.header('Forecasted Dataframe Plot')
    st.write(model.plot(forecast))
else:
    st.warning('Please Click on Prediction')
st.write('---')
