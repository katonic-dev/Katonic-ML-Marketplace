import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Anti-Money Laundering Activity Scoring', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Anti-Money Laundering Activity Scoring')
st.sidebar.write('---')

st.write("""
# Anti-Money Laundering Activity Scoring App
This app predicts which cases will result in a **SAR filing**!
""")
st.write('---')

# Loads Dataset
data_path = 'money_laudering_data.csv'
data_df = pd.read_csv(data_path, encoding = 'ISO-8859-1')
data_df = data_df.drop(['csrNotes'], axis=1)
data_df = data_df[data_df['income'].notna()]
st.write(data_df.head(20))

# showing fig1
st.subheader('Total Merchant Credits by State (90 days)')
df1 = data_df.groupby('state').agg({'totalMerchCred90d': 'mean'})
st.bar_chart(data=df1, width=0, height=0, use_container_width=True)

# showing fig2
st.subheader('Total Spend vs Suspicious Activity by state (90 days)')
df1 = data_df.where(data_df['SAR'] == 1).groupby('state').agg({'SAR': 'count'})
df2 = data_df.where(data_df['SAR'] == 0).groupby('state').agg({'SAR': 'count'})
df_perc = (df1/(df2+df1))
df3 = data_df.groupby('state').agg({'totalSpend90d': 'mean'})
df_perc['totalSpend90d'] = df3.totalSpend90d
st.bar_chart(data=df_perc, width=0, height=0, use_container_width=True)

def user_input_features():
    
    kycRiskScore = st.sidebar.slider('Account relationship (Know Your Customer) score', 0, 6, 3)
    income = st.sidebar.number_input('Annual income', 1, 344700, 51471)
    tenureMonths = st.sidebar.slider('Account tenure in months', 0, 232, 200)
    creditScore = st.sidebar.slider('Credit bureau score', 554, 800, 712)
    state = st.sidebar.select_slider('Account billing address state', options=['PA', 'NY', 'MA', 'NJ', 'CT', 'ME', 'RI', 'VT', 'NH'])
    nbrPurchases90d = st.sidebar.slider('No. of purchases in last 90 days', 0, 766, 26)
    avgTxnSize90d = st.sidebar.number_input('Average transaction size in last 90 days', 0.0, 2315.44, 149.67)
    totalSpend90d = st.sidebar.number_input('Total spend in last 90 days', 0.0, 1218718.71, 4019.31)
    nbrDistinctMerch90d = st.sidebar.slider('No. of distinct merchants purchased at in last 90 days', 0, 362, 13)
    nbrMerchCredits90d = st.sidebar.slider('No. of credits from merchants in last 90 days', 0, 82, 32)
    nbrMerchCreditsRndDollarAmt90d = st.sidebar.slider('No. of credits from merchants in round dollar amounts in last 90 days', 0, 13, 2)
    totalMerchCred90d = st.sidebar.number_input('Total merchant credit amount in last 90 days', 0.0, 100379.13, 404.72)
    nbrMerchCreditsWoOffsettingPurch = st.sidebar.slider('No. of merchant credits without an offsetting purchase in last 90 days', 0, 35, 12)
    nbrPayments90d = st.sidebar.slider('No. of payments in last 90 days', 2, 12, 3)
    totalPaymentAmt90d = st.sidebar.number_input('Total payment amount in last 90 days', 60.0, 2063840.73, 3467.28)
    overpaymentAmt90d = st.sidebar.number_input('Total amount overpaid in last 90 days', 0.0, 845122.02, 464.88)
    overpaymentInd90d = st.sidebar.slider('Indicator that account was overpaid in last 90 days', 0, 1, 1)
    nbrCustReqRefunds90d = st.sidebar.slider('No. refund requests by the customer in last 90 days', 1, 4, 1)
    totalRefundsToCust90d = st.sidebar.number_input('Total refund amount in last 90 days', 0.0, 845158.58, 508.90)
    nbrPaymentsCashLike90d = st.sidebar.slider('No. of cash like payments (e.g., money orders) in last 90 days', 0, 10, 2)
    maxRevolveLine = st.sidebar.number_input('Maximum revolving line of credit', 3000, 34000, 12024)
    indOwnsHome = st.sidebar.slider('Indicator that the customer owns a home', 0, 1, 0)
    nbrInquiries1y = st.sidebar.slider('No. of credit inquiries in the past year', 0, 11, 2)
    nbrCollections3y = st.sidebar.slider('No. of collections in the past year', 0, 4, 1)
    nbrWebLogins90d = st.sidebar.slider('No. of logins to the bank website in the last 90 days', 0, 97, 7)
    nbrPointRed90d = st.sidebar.slider('No. of loyalty point redemptions in the last 90 days', 0, 5, 2)

    data = {
      'kycRiskScore': kycRiskScore,
      'income': income,
      'tenureMonths': tenureMonths,
      'creditScore': creditScore,
      'state': state,
      'nbrPurchases90d': nbrPurchases90d,
      'avgTxnSize90d': avgTxnSize90d,
      'totalSpend90d': totalSpend90d,
      'nbrDistinctMerch90d': nbrDistinctMerch90d,
      'nbrMerchCredits90d': nbrMerchCredits90d,
      'nbrMerchCreditsRndDollarAmt90d': nbrMerchCreditsRndDollarAmt90d,
      'totalMerchCred90d': totalMerchCred90d,
      'nbrMerchCreditsWoOffsettingPurch': nbrMerchCreditsWoOffsettingPurch,
      'nbrPayments90d': nbrPayments90d,
      'totalPaymentAmt90d': totalPaymentAmt90d,
      'overpaymentAmt90d': overpaymentAmt90d,
      'overpaymentInd90d': overpaymentInd90d,
      'nbrCustReqRefunds90d': nbrCustReqRefunds90d,
      'totalRefundsToCust90d': totalRefundsToCust90d,
      'nbrPaymentsCashLike90d': nbrPaymentsCashLike90d,
      'maxRevolveLine': maxRevolveLine,
      'indOwnsHome': indOwnsHome,
      'nbrInquiries1y': nbrInquiries1y,
      'nbrCollections3y': nbrCollections3y,
      'nbrWebLogins90d': nbrWebLogins90d,
      'nbrPointRed90d': nbrPointRed90d,
    }
    return pd.DataFrame(data, index=[0])


# Main Panel
data_df['state'] = data_df['state'].replace({'PA': 1, 'NY': 2, 'MA': 3, 'NJ': 4, 'CT': 5, 'ME': 6, 'RI': 7, 'VT': 8, 'NH': 9})
data_df = data_df.drop(['ALERT', 'indCustReqRefund90d', 'PEP'], axis=1)

X = data_df.drop(['SAR'], axis=1)
y = data_df['SAR']

min_max_scaler = MinMaxScaler()
X = min_max_scaler.fit_transform(X)

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

df['state'] = df['state'].replace({'PA': 1, 'NY': 2, 'MA': 3, 'NJ': 4, 'CT': 5, 'ME': 6, 'RI': 7, 'VT': 8, 'NH': 9})

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Money Laundering Intelligence Predictions')
    label = 'SAR filing' if prediction > 0.5 else 'No SAR filing'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')