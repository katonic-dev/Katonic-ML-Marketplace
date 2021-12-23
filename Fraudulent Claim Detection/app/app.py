import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects  as go
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Fraudulent Claim Detection App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Fraudulent Claim Detection')
st.sidebar.write('---')

st.write("""
# Fraudulent Claim Detection App

This app predict whether the **Claim is Fraud or Not**!
""")
st.write('---')

# Loads the Dataset
data_path = 'fraudulent_claim_insurance.csv'
data_df = pd.read_csv(data_path)
data_df = data_df.drop(['DATE', 'ID', 'LOCALITY', 'CLAIM_DESCRIPTION'], axis=1)
data_df = data_df[data_df['REGION'].notna()]
st.write(data_df.head(20))

data_df['FRAUD_str'] = data_df['FRAUD'].replace(0, 'Not FRAUD').replace(1, 'FRAUD')

# showing fig1
st.subheader('Average Claim Fraud By Metric')
st.bar_chart(data=data_df.groupby('FRAUD_str').agg({'NUM_PI_CLAIM': 'mean', 'DISTINCT_PARTIES_ON_CLAIM': 'mean'}), width=0, height=0, use_container_width=True)

# showing fig2
st.subheader('Policy Length Distribution ')
fig = px.bar(data_frame=data_df.groupby(['POLICY_LENGTH']).agg({'NEW_VEHICLE_BEFORE_CLAIM': 'mean'}), y='NEW_VEHICLE_BEFORE_CLAIM', barmode='group')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
fig.update_yaxes(title_text = 'NEW_VEHICLE_BEFORE_CLAIM')
fig.update_xaxes(tickangle = 0, title_text='Policy Length')
st.plotly_chart(fig, use_container_width=False)

# showing fig3
st.subheader('Fraud by Region')
df1 = data_df.where(data_df['FRAUD'] == 1).groupby('REGION').agg({'FRAUD': 'count'})
df2 = data_df.where(data_df['FRAUD'] == 0).groupby('REGION').agg({'FRAUD': 'count'})
df_perc = (df1/(df2+df1))
fig = px.bar(data_frame=df_perc, y='FRAUD', barmode='group')
fig.update_xaxes(tickangle = 45)
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

data_df = MultiColumnLabelEncoder(columns = ['REGION']).fit_transform(data_df)

def user_input_features():

    REGION = st.sidebar.selectbox(
        'Customer’s region', 
        options=['OX', 'LN', 'SL', 'LA', 'CM', 'BT', 'NR', 'NE', 'M', 'SR', 'BB',
        'IP', 'TR', 'FK', 'HU', 'BS', 'B', 'ME', 'CF', 'EX', 'NG', 'PO',
        'CH', 'WV', 'SA', 'N', 'EH', 'SG', 'E', 'YO', 'BA', 'BR', 'S',
        'BH', 'LL', 'IV', 'PE', 'LS', 'BD', 'TA', 'PA', 'DN', 'MK', 'AB',
        'AL', 'SY', 'CR', 'NP', 'WS', 'WN', 'SE', 'HG', 'CO', 'PL', 'WA',
        'CW', 'LE', 'WF', 'SS', 'BL', 'SO', 'KA', 'L', 'SM', 'G', 'TQ',
        'KY', 'TW', 'HX', 'DH', 'RM', 'DT', 'TN', 'PR', 'HA', 'GU', 'BN',
        'W', 'NN', 'TS', 'SN', 'WD', 'KT', 'IM', 'DY', 'DL', 'CB', 'ML',
        'TD', 'LU', 'HP', 'FY', 'DA', 'ST', 'DE', 'EN', 'PH', 'WR', 'CA',
        'RH', 'HD', 'OL', 'TF', 'RG', 'UB', 'SK', 'CV', 'CT', 'GL', 'DG',
        'DD', 'IG', 'HR', 'SW', 'SP', 'KW', 'NW', 'LD', 'EW', 'JE', 'HS',
        'NC', 'GY', 'ECY', 'WG', 'ZE', 'ECR'])
    GENDER = st.sidebar.selectbox('Customer’s gender',['MALE', 'FEMALE'])
    CLAIM_POLICY_DIFF_A = st.sidebar.slider('Internal Claim Policy A', 0, 1, 1)
    CLAIM_POLICY_DIFF_B = st.sidebar.slider('Internal Claim Policy B', 0, 1, 0)
    CLAIM_POLICY_DIFF_C = st.sidebar.slider('Internal Claim Policy C', 0, 1, 0)
    CLAIM_POLICY_DIFF_D = st.sidebar.slider('Internal Claim Policy D', 0, 1, 0)
    CLAIM_POLICY_DIFF_E = st.sidebar.slider('Internal Claim Policy E', 0, 1, 0)
    POLICY_CLAIM_DAY_DIFF = st.sidebar.slider('Number of days since policy taken', 10, 58, 42)
    DISTINCT_PARTIES_ON_CLAIM = st.sidebar.slider('Number of people on claim', 1, 28, 10)
    CLM_AFTER_RNWL = st.sidebar.slider('Renewal History', 0, 1, 0)
    NOTIF_AFT_RENEWAL = st.sidebar.slider('Renewal History Notification',  0, 1, 1)
    CLM_DURING_CAX = st.sidebar.slider('Cancellation claim', 0, 1, 1)
    COMPLAINT = st.sidebar.slider('Customer complaint', 0, 1, 1)
    CLM_before_PAYMENT = st.sidebar.slider('Claim before premium paid', 0, 1, 0)
    PROP_before_CLM = st.sidebar.slider('Property before Claim', 0, 1, 1)
    NCD_REC_before_CLM = st.sidebar.slider('NCD Record before Claim', 0, 1, 1)
    NOTIF_DELAY = st.sidebar.slider('Delay in notification', 0, 1, 1)
    ACCIDENT_NIGHT = st.sidebar.slider('Night time accident', 0, 1, 0)
    NUM_PI_CLAIM = st.sidebar.slider('Number of personal injury claims', 0, 18, 12)
    NEW_VEHICLE_BEFORE_CLAIM = st.sidebar.slider('New Vehicle Before Claim (Vehicle History)', 0, 1, 1)
    PERSONAL_INJURY_INDICATOR = st.sidebar.slider('Personal Injury flag', 0, 1, 0)
    CLAIM_TYPE_ACCIDENT = st.sidebar.slider('Claim Type Accident', 0, 1, 1)
    CLAIM_TYPE_FIRE = st.sidebar.slider('Claim Type Fire', 0, 1, 0)
    CLAIM_TYPE_MOTOR_THEFT = st.sidebar.slider('Claim Type Motor Theft', 0, 1, 0)
    CLAIM_TYPE_OTHER = st.sidebar.slider('Claim Type Other', 0, 1, 0)
    CLAIM_TYPE_WINDSCREEN = st.sidebar.slider('Claim Type Windscreen', 0, 1, 0)
    LOCAL_TEL_MATCH = st.sidebar.slider('Internal Rule Matching-Local Tel', 0, 1, 1)
    LOCAL_M_CLM_ADD_MATCH = st.sidebar.slider('Internal Rule Matching-Local M Claim Add', 0, 1, 0)
    LOCAL_M_CLM_PERS_MATCH = st.sidebar.slider('Internal Rule Matching-Local M Claim Pers', 0, 1, 0)
    LOCAL_NON_CLM_ADD_MATCH = st.sidebar.slider('Internal Rule Matching-Local Non Claim Add', 0, 1, 0)
    LOCAL_NON_CLM_PERS_MATCH = st.sidebar.slider('Internal Rule Matching-Local NOn Claim Pers', 0, 1, 0)
    federal_TEL_MATCH = st.sidebar.slider('Internal Rule Matching-federal Tel', 0, 1, 0)
    federal_CLM_ADD_MATCH = st.sidebar.slider('Internal Rule Matching-federal Claim Add', 0, 1, 0)
    federal_CLM_PERS_MATCH = st.sidebar.slider('Internal Rule Matching-federal Claim Pers', 0, 1, 0)
    federal_NON_CLM_ADD_MATCH = st.sidebar.slider('Internal Rule Matching-federal Non Claim Add', 0, 1, 0)
    federal_NON_CLM_PERS_MATCH = st.sidebar.slider('Internal Rule Matching-federal Non claim Pers', 0, 1, 0)
    SCR_LOCAL_RULE_COUNT = st.sidebar.slider('Internal Rule Matching-SCR Local Rule Count', 0, 6, 5)
    SCR_NAT_RULE_COUNT = st.sidebar.slider('Internal Rule Matching-SCR Nat Rule Count', 0, 4, 3)
    RULE_MATCHES = st.sidebar.slider('Rule Matches', 0, 1, 1)

    data = {
        'REGION': REGION, 
        'GENDER': GENDER, 
        'CLAIM_POLICY_DIFF_A': CLAIM_POLICY_DIFF_A,
        'CLAIM_POLICY_DIFF_B': CLAIM_POLICY_DIFF_B, 
        'CLAIM_POLICY_DIFF_C': CLAIM_POLICY_DIFF_C, 
        'CLAIM_POLICY_DIFF_D': CLAIM_POLICY_DIFF_D,
        'CLAIM_POLICY_DIFF_E': CLAIM_POLICY_DIFF_E, 
        'POLICY_CLAIM_DAY_DIFF': POLICY_CLAIM_DAY_DIFF,
        'DISTINCT_PARTIES_ON_CLAIM': DISTINCT_PARTIES_ON_CLAIM, 
        'CLM_AFTER_RNWL': CLM_AFTER_RNWL, 
        'NOTIF_AFT_RENEWAL': NOTIF_AFT_RENEWAL,
        'CLM_DURING_CAX': CLM_DURING_CAX, 
        'COMPLAINT': COMPLAINT, 
        'CLM_before_PAYMENT': CLM_before_PAYMENT, 
        'PROP_before_CLM': PROP_before_CLM,
        'NCD_REC_before_CLM': NCD_REC_before_CLM, 
        'NOTIF_DELAY': NOTIF_DELAY, 
        'ACCIDENT_NIGHT': ACCIDENT_NIGHT, 
        'NUM_PI_CLAIM': NUM_PI_CLAIM,
        'NEW_VEHICLE_BEFORE_CLAIM': NEW_VEHICLE_BEFORE_CLAIM, 
        'PERSONAL_INJURY_INDICATOR': PERSONAL_INJURY_INDICATOR,
        'CLAIM_TYPE_ACCIDENT': CLAIM_TYPE_ACCIDENT, 
        'CLAIM_TYPE_FIRE': CLAIM_TYPE_FIRE, 
        'CLAIM_TYPE_MOTOR_THEFT': CLAIM_TYPE_MOTOR_THEFT,
        'CLAIM_TYPE_OTHER': CLAIM_TYPE_OTHER, 
        'CLAIM_TYPE_WINDSCREEN': CLAIM_TYPE_WINDSCREEN, 
        'LOCAL_TEL_MATCH': LOCAL_TEL_MATCH,
        'LOCAL_M_CLM_ADD_MATCH': LOCAL_M_CLM_ADD_MATCH, 
        'LOCAL_M_CLM_PERS_MATCH': LOCAL_M_CLM_PERS_MATCH,
        'LOCAL_NON_CLM_ADD_MATCH': LOCAL_NON_CLM_ADD_MATCH, 
        'LOCAL_NON_CLM_PERS_MATCH': LOCAL_NON_CLM_PERS_MATCH,
        'federal_TEL_MATCH': federal_TEL_MATCH, 
        'federal_CLM_ADD_MATCH': federal_CLM_ADD_MATCH, 
        'federal_CLM_PERS_MATCH': federal_CLM_PERS_MATCH,
        'federal_NON_CLM_ADD_MATCH': federal_NON_CLM_ADD_MATCH, 
        'federal_NON_CLM_PERS_MATCH': federal_NON_CLM_PERS_MATCH,
        'SCR_LOCAL_RULE_COUNT': SCR_LOCAL_RULE_COUNT, 
        'SCR_NAT_RULE_COUNT': SCR_NAT_RULE_COUNT, 
        'RULE_MATCHES': RULE_MATCHES
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

data_df = data_df.drop(['POLICY_LENGTH', 'FRAUD_str'], axis=1)

X = data_df.drop(['FRAUD'], axis=1)
y = data_df['FRAUD']

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

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

df = MultiColumnLabelEncoder(columns = ['REGION']).fit_transform(df)
df['GENDER'] = df['GENDER'].replace('MALE', 1).replace('FEMALE', 0)

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Fraud Claim Detection Predictions')
    label = 'Fruadulent' if prediction > 0.5 else 'Legit'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')



