import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects  as go
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Bank Customer Churn Prediction', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Bank Customer Churn Prediction')
st.sidebar.write('---')

st.write("""
# Bank Customer Churn Prediction App

This app predict **Whether Customers are Planning to Churn or remain.**!
""")
st.write('---')

# Loads the Dataset
data_path = 'bank_customer_churn.csv'
data_df = pd.read_csv(data_path)
data_df = data_df.drop(['RowNumber', 'Surname'], axis=1)
st.write(data_df.head(20))

# showing fig1
st.subheader('Proportion of customer churned and retained')
labels = 'Exited', 'Retained'
sizes = [data_df.Exited[data_df['Exited']==1].count(), data_df.Exited[data_df['Exited']==0].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.2, 0, 0])])
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('Geography relation with Customer Churn')
count_df = data_df.groupby(by=['Geography', 'Exited']).size().reset_index(name='counts')
fig = px.bar(data_frame=count_df, x='Geography', y='counts', color='Exited', barmode='group')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

class MultiColumnLabelEncoder:
    def __init__(self,columns = None):
        self.columns = columns

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)

data_df = MultiColumnLabelEncoder(columns = ['Geography', 'Gender']).fit_transform(data_df)

def user_input_features():

    CreditScore = st.sidebar.slider('Credit Score', 350, 850, 650)
    Geography = st.sidebar.select_slider('Geography', options=['Spain', 'France', 'Germany'])
    Gender = st.sidebar.select_slider('Gender', options=['Male', 'Female'])
    Age = st.sidebar.slider('Customer Age', 18, 92, 38)
    Tenure = st.sidebar.slider('Account tenure in months', 0, 10, 5)
    Balance = st.sidebar.number_input('Balance', 0.0, 250898.09, 76485.88)
    NumOfProducts = st.sidebar.slider('No. Of Products', 1, 4, 1)
    HasCrCard = st.sidebar.select_slider('Has Credit Card', options=[0, 1])
    IsActiveMember = st.sidebar.select_slider('Is Customer Active Member', options=[0, 1])
    EstimatedSalary = st.sidebar.number_input('Estimated Salary of the Customer', 11.58, 199992.48, 100090.23)

    data = {
        'CreditScore': CreditScore, 
        'Geography': Geography,
        'Gender': Gender,
        'Age': Age, 
        'Tenure': Tenure, 
        'Balance': Balance, 
        'NumOfProducts': NumOfProducts,
        'HasCrCard': HasCrCard, 
        'IsActiveMember': IsActiveMember, 
        'EstimatedSalary': EstimatedSalary, 
    }
    return pd.DataFrame(data, index=[0])

# Main Panel
data_df = data_df.drop(['CustomerId'], axis=1)

X = data_df.drop(['Exited'], axis=1)
y = data_df['Exited']

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
df = MultiColumnLabelEncoder(columns = ['Geography', 'Gender']).fit_transform(df)

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Customer Churn Predictions')
    label = 'Exited' if prediction > 0.5 else 'Not Exited'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')

