import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Predict Likelihood of Loan Default App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Predict Likelihood of Loan Default')
st.sidebar.write('---')

st.write("""
# Predict Likelihood of Loan Default App

This app predicts **if someone is going to default this may lead to intervention steps such as sending earlier notices or rejecting loan applications**.!
""")
st.write('---')

# Loads Dataset
data_path = 'loan_default_data.csv'
data_df = pd.read_csv(data_path, encoding = 'ISO-8859-1')
st.write(data_df.head(20))

# showing fig1
st.subheader('Average Income by Status of Loan (Yes = Loan Defaulted)')
df1 = data_df.groupby('loan_is_bad').agg({'annual_inc': 'mean'})
fig = px.bar(df1)
fig.update_yaxes(title_text = 'Average Income by Status of Loan')
fig.update_xaxes(tickangle = 0, title_text='Loan is Bad')
fig.update_layout(
    barmode='relative', 
    title_text='Relative Barmode', 
    uniformtext_minsize=8, 
    uniformtext_mode='hide', 
    margin=dict(t=0, b=0, l=0, r=0)
)
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('% of Loans Defaulting by Employment Length')
avg_value_df = data_df.groupby('emp_length').agg({'loan_is_bad':'mean'})
fig = px.bar(avg_value_df)
fig.update_yaxes(title_text = '% of Loans Defaulting by Employment Length')
fig.update_xaxes(tickangle = 0, title_text='Employment Length')
fig.update_layout(
    barmode='relative', 
    title_text='Relative Barmode', 
    uniformtext_minsize=8, 
    uniformtext_mode='hide', 
    margin=dict(t=0, b=0, l=0, r=0)
)
st.plotly_chart(fig, use_container_width=False)

# showing fig3
st.subheader('% of Loans Defaulting by State')
avg_value_df = data_df.groupby('addr_state').agg({'loan_is_bad':'mean'})
fig = px.bar(avg_value_df)
fig.update_yaxes(title_text = '% of Loans Defaulting by State')
fig.update_xaxes(tickangle = 0, title_text='Address State')
fig.update_layout(barmode='relative', title_text='Relative Barmode')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

data_df = data_df.drop(
    ['id', 'member_id', 'revol_util', 'emp_title', 'title', 'zip_code', 'earliest_cr_line', 'mths_since_last_delinq', 
    'mths_since_last_record', 'mths_since_last_major_derog'], 
    axis=1
)
data_df = data_df[data_df['emp_length'].notna()]
data_df = data_df[data_df['tot_coll_amt'].notna()]
data_df = data_df[data_df['tot_cur_bal'].notna()]

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
    columns = ['grade', 'sub_grade', 'home_ownership', 'purpose', 'addr_state', 'initial_list_status', 'application_type', 
    'loan_is_bad']
).fit_transform(data_df)

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    
    loan_amnt = st.sidebar.number_input('Loan Amount', 1000, 35000, 13905)
    funded_amnt = st.sidebar.number_input('Funded Amount', 1000, 35000, 13000)
    installment = st.sidebar.number_input('Installment', 25.81, 1388.45, 437.08)
    grade = st.sidebar.selectbox(
        'Grade', 
        options=['A', 'B', 'C', 'E', 'D', 'F', 'G']
    )
    sub_grade = st.sidebar.selectbox(
        'Sub Grade', 
        options=['A2',  'B2',  'C4',  'A4',  'B4',  'B1',  'E1',  'D1',  'C5',  'C3',  'B3',  'B5',  'A5',  'D5',  'C1',  
        'E3',  'A1',  'D4',  'C2',  'A3',  'F3',  'D3',  'E2',  'E5',  'F2',  'F1',  'D2',  'E4',  'G3',  'F4',  'F5',  
        'G2',  'G5',  'G1',  'G4']
    )
    emp_length = st.sidebar.number_input('Employment Length', 1, 10, 5)
    home_ownership = st.sidebar.selectbox('Home Ownership', options=['MORTGAGE', 'RENT', 'OWN', 'OTHER'])
    annual_inc = st.sidebar.number_input('Annual Income', 5000, 7141778, 71350)
    purpose = st.sidebar.selectbox(
        'Purpose', 
        options= ['debt_consolidation', 'credit_card', 'home_improvement', 'other', 'major_purchase', 'small_business', 
        'car', 'wedding', 'medical', 'moving', 'house', 'vacation', 'renewable_energy']
    )
    addr_state = st.sidebar.selectbox(
        'Address State', 
        options=['TX',  'NJ',  'OH',  'CT',  'CO',  'CA',  'VA',  'DE',  'FL',  'MA',  'MI',  'OR',  'PA',  'NY',  'GA',  
        'IL',  'MN',  'AZ',  'AR',  'NC',  'KY',  'LA',  'WA',  'MT',  'IN',  'KS',  'WI',  'SD',  'VT',  'AL',  'MD',  
        'NM',  'RI',  'MO',  'OK',  'UT',  'AK', 'NV',  'SC',  'WY',  'HI',  'NH',  'DC',  'WV',  'TN',  'NE']
    )
    dti = st.sidebar.number_input('Debt To Income', 0.0, 34.99, 17.37)
    delinq_2yrs = st.sidebar.selectbox('Delinquent 2 Yrs', options=[0, 18, 5])
    inq_last_6mths = st.sidebar.selectbox('Inquiry Last 6 Months', options=[1, 8, 2])
    open_acc = st.sidebar.number_input('Open Account', 0, 53, 11)
    pub_rec = st.sidebar.selectbox('Public Reccords', options=[0, 1, 8])
    revol_bal = st.sidebar.number_input('Revolving Balance', 0, 1743266, 16019)
    total_acc = st.sidebar.number_input('Total Account', 2, 99, 24)
    initial_list_status = st.sidebar.selectbox('Initial List Status', options=['f', 'w'])
    collections_12_mths_ex_med = st.sidebar.selectbox('Collections 12 Months Ex Medic', options=[0, 1, 2])
    application_type = st.sidebar.selectbox('Application Type', options=['INDIVIDUAL'])
    acc_now_delinq = st.sidebar.selectbox('Account now Delinquent ', options=[0, 1, 2, 4])
    tot_coll_amt = st.sidebar.number_input('Total Collected Amountt', 0, 55009, 1000)
    tot_cur_bal = st.sidebar.number_input('Total Current Balance', 0, 8000078, 133676)

    data = {
        'loan_amnt': loan_amnt, 
        'funded_amnt': funded_amnt, 
        'installment': installment, 
        'grade': grade, 
        'sub_grade': sub_grade,
        'emp_length': emp_length, 
        'home_ownership': home_ownership, 
        'annual_inc': annual_inc, 
        'purpose': purpose, 
        'addr_state': addr_state, 
        'dti': dti, 
        'delinq_2yrs': delinq_2yrs, 
        'inq_last_6mths': inq_last_6mths, 
        'open_acc': open_acc,
        'pub_rec': pub_rec, 
        'revol_bal': revol_bal, 
        'total_acc': total_acc,
        'initial_list_status': initial_list_status, 
        'collections_12_mths_ex_med': collections_12_mths_ex_med, 
        'application_type': application_type,
        'acc_now_delinq': acc_now_delinq, 
        'tot_coll_amt': tot_coll_amt, 
        'tot_cur_bal': tot_cur_bal, 
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

X = data_df.drop(['loan_is_bad'], axis=1)
y = data_df['loan_is_bad']

min_max_scaler = MinMaxScaler()
X = min_max_scaler.fit_transform(X)

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'finalized_model.sav'
if agree:
    # Build Regression Model
    model = LinearRegression() 
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
    columns = ['grade', 'sub_grade', 'home_ownership', 'purpose', 'addr_state', 'initial_list_status', 'application_type']
).fit_transform(df)

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Loan Analysis Intelligence Predictions')
    label = 'Loan is Good' if prediction > 0.5 else 'Loan is Bad'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Score: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
    st.write('---')
