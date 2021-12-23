import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Telecom Customer Churn Prediction App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Telecom Customer Churn Prediction')
st.sidebar.write('---')

st.write("""
# Telecom Customer Churn Prediction App

This app predict **Whether Customers are Planning to Churn or Remain.**!
""")
st.write('---')

# Loads the Dataset
data_path = 'customer_churn.csv'
data_df = pd.read_csv(data_path)
st.write(data_df.head(20))

# showing fig1
st.subheader('Customer Contract vs Churn Count')
fig = plt.figure(figsize=(10, 4))
sns.countplot(y='Contract', hue='Churn', data=data_df, palette='Blues_d')
st.pyplot(fig)

# showing fig2
st.subheader('Customer Tenure vs Churn Relation')
fig = plt.figure(figsize=(10, 4))
sns.lineplot(x='tenure', y='Churn', data=data_df)
st.pyplot(fig)

# showing fig3
st.subheader('Online Security to Churn Count')
fig = plt.figure(figsize=(10, 4))
sns.countplot(y='OnlineSecurity', hue='Churn', data=data_df, palette='Blues_d')
st.pyplot(fig)

# showing fig4
st.subheader('Monthly Charges with Customer Churn')
fig = plt.figure(figsize=(10, 4))
sns.stripplot(x='Churn', y='MonthlyCharges', data=data_df)
st.pyplot(fig)

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

data_df = MultiColumnLabelEncoder(
    columns = list(data_df.select_dtypes(include=['object']).columns)
).fit_transform(data_df)

def user_input_features():

    gender = st.sidebar.selectbox('Gender', options=['Male', 'Female'])
    SeniorCitizen = st.sidebar.selectbox('Senior Citizen', options=[0, 1])
    Partner = st.sidebar.selectbox('Partner', options=[0, 1])
    Dependents = st.sidebar.selectbox('Dependents', options=['Yes', 'No'])
    PhoneService = st.sidebar.selectbox('Phone Service', options=['Yes', 'No'])
    MultipleLines = st.sidebar.selectbox('Multiple Lines', options=['No', 'Yes', 'No internet service'])
    DeviceProtection = st.sidebar.selectbox('Device Protection', options=['Yes', 'No'])
    StreamingTV = st.sidebar.selectbox('StreamingTV', options=['Yes', 'No'])
    StreamingMovies = st.sidebar.selectbox('StreamingMovies', options=['No', 'Yes'])
    tenure = st.sidebar.slider('Tenure with company', 0, 80, 23)
    OnlineSecurity = st.sidebar.selectbox('Internet Service', options=['No', 'Yes', 'No internet service'])
    TechSupport = st.sidebar.selectbox('Tech Support', options=['No', 'Yes', 'No internet service'])
    Contract = st.sidebar.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'])
    MonthlyCharges = st.sidebar.slider('Monthly Charges', 0.0, 120.0, 50.0)
    TotalCharges = st.sidebar.slider('Temperature Indicator', 0.0, 7000.0, 450.0)
    InternetService = st.sidebar.selectbox('Internet Service', options=['DSL', 'Fiber optic', 'No'])
    OnlineBackup = st.sidebar.selectbox('Online Backup', options=['Yes', 'No', 'No internet service'])
    PaperlessBilling = st.sidebar.selectbox('Paperless Billing', options=['Yes', 'No'])
    PaymentMethod = st.sidebar.selectbox('Payment Method', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'])

    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure, 
        'PhoneService': PhoneService, 
        'MultipleLines': MultipleLines, 
        'InternetService': InternetService, 
        'OnlineSecurity': OnlineSecurity, 
        'OnlineBackup': OnlineBackup, 
        'DeviceProtection': DeviceProtection, 
        'TechSupport': TechSupport, 
        'StreamingTV': StreamingTV, 
        'StreamingMovies': StreamingMovies, 
        'Contract': Contract, 
        'PaperlessBilling': PaperlessBilling, 
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges, 
        'TotalCharges': TotalCharges
    }
    return pd.DataFrame(data, index=[0])

# Main Panel
data_df = data_df.drop(['customerID'], axis=1)

X = data_df.drop(['Churn'], axis=1)
y = data_df['Churn']

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'finalized_model.sav'
if agree:
    # Build Regression Model
    model = RandomForestClassifier()
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

df = MultiColumnLabelEncoder(
    columns = list(df.select_dtypes(include=['object']).columns)
    # columns = ['tenure', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'TechSupport', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
).fit_transform(df)

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Customer Churn Predictions')
    label = 'Churned' if prediction > 0.5 else 'Remain'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')
