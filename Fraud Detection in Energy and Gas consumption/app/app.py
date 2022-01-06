import pandas as pd
import plotly.graph_objects  as go
import plotly.express as px
import pickle
import requests
from io import BytesIO
from PIL import Image
from lightgbm import LGBMClassifier
import streamlit as st

response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Fraud Detection in Energy and Gas consumption', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Fraud Detection in Energy and Gas consumption')
st.sidebar.write('---')

st.write("""
# Fraud Detection in Energy and Gas consumption
This app predicts which **clients are highly likely to commit fraudulent activities.!**
""")
st.write('---')

# Loads Dataset

client_train = pd.read_csv('client_train.csv', encoding = 'ISO-8859-1')
invoice_train = pd.read_csv('invoice_train.csv', encoding = 'ISO-8859-1')
st.write('**Client Information**')
st.write(client_train.head(20))
st.write('---')
st.write('**Client Invoice**')
st.write(invoice_train.tail(20))
st.write('---')

# showing fig1
st.subheader('Percentage of Client involved in fraudulent activities')
labels = 'Fraud', 'Not-Fraud'
sizes = [client_train.target[client_train['target']==1].count(), client_train.target[client_train['target']==0].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.05, 0, 0])])
fig.update_traces(marker=dict(colors=['indigo', 'forestgreen']))
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# District
st.subheader('District involved in Fraudulent activities')
ds = client_train.groupby(['district'])['client_id'].count()
fig = px.bar(data_frame=ds)
fig.update_layout(margin=dict(t=50, b=50, l=200, r=0)) 
st.plotly_chart(fig, use_container_width=False)

# Region
st.subheader('Region involved in Fraudulent activities')
ds = client_train.groupby(['region'])['client_id'].count()
fig = px.bar(data_frame=ds)
fig.update_layout(margin=dict(t=50, b=50, l=200, r=0)) 
st.plotly_chart(fig, use_container_width=False)

#client_catg
st.subheader('Client categories')
labels = 'cat-11', 'cat-12','cat-51'
sizes = [client_train.client_catg[client_train['client_catg']==11].count(), client_train.client_catg[client_train['client_catg']==12].count(),
         client_train.client_catg[client_train['client_catg']==51].count()  ]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.08, 0, 0])])
fig.update_traces(marker=dict(colors=['mediumpurple','indigo', 'forestgreen']))
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

def user_input_features():
    
    st.sidebar.subheader('Client Details')
    client_id = st.sidebar.number_input('Unique id of Client', 1, 344700, 51471)
    district = st.sidebar.selectbox('District of the client', ('60','62','63','69'))
    client_catg = st.sidebar.selectbox('Category Client belongs to', ('11','12','51'))
    region = st.sidebar.slider('Region where the client is', 100,400,1)
    creation_Date = st.sidebar.date_input('Date client joined')
    st.sidebar.write('---')
    st.sidebar.subheader('Client Invoice Details')
    invoice_Date = st.sidebar.date_input('Date of the invoice')
    tarif_type = st.sidebar.slider('Type of Tax',1,100,1)
    counter_number = st.sidebar.number_input('counter number', 1,900000, 1)
    counter_statue = st.sidebar.slider('Counter status', 0, 20, 1)
    counter_code = st.sidebar.number_input('counter code', 0, 800, 1)
    reading_remarque = st.sidebar.number_input('reading score during the visit', 0, 20, 1)
    counter_coefficient = st.sidebar.slider('Additional coefficient', 0, 20, 1)
    consommation_level_1 = st.sidebar.number_input('consumption level 1', 0, 10000, 1)
    consommation_level_2 = st.sidebar.number_input('consumption level 2', 0, 10000,1)
    consommation_level_3 = st.sidebar.number_input('consumption level 3', 0, 10000, 1)
    consommation_level_4 = st.sidebar.number_input('consumption level 4', 0, 10000, 1)
    old_index = st.sidebar.number_input('old index', 1, 155648, 1)
    new_index = st.sidebar.number_input('new index', 0, 157980, 1)
    months_number = st.sidebar.slider('month number', 0, 50, 2)
    counter_type = st.sidebar.selectbox('counter type', ('GAZ','ELEC'))
    
    client = {
        'district':  district,
        'client_id': client_id,
        'client_catg': client_catg,
        'region': region,
        'creation_date': creation_Date,
      }
    invoice={
      'client_id': client_id,
      'invoice_date': invoice_Date,
      'tarif_type': tarif_type,
      'counter_number': counter_number,
      'counter_statue': counter_statue,
      'counter_code': counter_code,
      'reading_remarque': reading_remarque,
      'counter_coefficient': counter_coefficient,
      'consommation_level_1': consommation_level_1,
      'consommation_level_2': consommation_level_2,
      'consommation_level_3': consommation_level_3,
      'consommation_level_4': consommation_level_4,
      'old_index': old_index,
      'new_index': new_index,
      'months_number': months_number,
      'counter_type': counter_type,
    }

    return pd.DataFrame(invoice, index=[0]), pd.DataFrame(client, index=[0])

p,q = user_input_features()

# Print specified input parameters
st.header('Specified Input parameters')
st.subheader('Client details')
st.write(q)
st.subheader('Invoice details')
st.write(p)
st.write('---')

for df in [invoice_train,p]:
    df['invoice_date'] = pd.to_datetime(df['invoice_date'])

d={"ELEC":0,"GAZ":1}
invoice_train['counter_type']=invoice_train['counter_type'].map(d)
p['counter_type']=invoice_train['counter_type'].map(d)

client_train['client_catg'] = client_train['client_catg'].astype('int')
client_train['district'] = client_train['district'].astype('int')
client_train['region'] = client_train['region'].astype('int')
q['client_catg'] = q['client_catg'].astype('int')
q['district'] = q['district'].astype('int')
q['region'] = q['region'].astype('int')

aggs = {
    'consommation_level_1': ['mean'],
    'consommation_level_2': ['mean'],
    'consommation_level_3': ['mean'],
    'consommation_level_4': ['mean'],
}

agg_trans = invoice_train.groupby(['client_id']).agg(aggs)
agg_trans.columns = ['_'.join(col).strip() for col in agg_trans.columns.values]
agg_trans.reset_index(inplace=True)
df = (invoice_train.groupby('client_id')
          .size()
          .reset_index(name='{}transactions_count'.format('1')))
agg_trans = pd.merge(df, agg_trans, on='client_id', how='left')

train = pd.merge(client_train,agg_trans, on='client_id', how='left')

aggs = {
    'consommation_level_1': ['mean'],
    'consommation_level_2': ['mean'],
    'consommation_level_3': ['mean'],
    'consommation_level_4': ['mean'],
}

agg_trans = p.groupby(['client_id']).agg(aggs)
agg_trans.columns = ['_'.join(col).strip() for col in agg_trans.columns.values]
agg_trans.reset_index(inplace=True)
df = (p.groupby('client_id')
          .size()
          .reset_index(name='{}transactions_count'.format('1')))
agg_trans = pd.merge(df, agg_trans, on='client_id', how='left')

test = pd.merge(q,agg_trans, on='client_id', how='left')
y=train['target']

train.drop(['target'],axis=1,inplace=True)

drop_col = ['client_id','creation_date']
for col in drop_col:
    if col in train.columns:
        train.drop([col],axis=1,inplace=True)
    if col in test.columns:
        test.drop([col],axis=1,inplace=True)

# to retrain
agree = st.checkbox('Check to retrain the model')
filename = 'final_model.sav'
if agree:
    # Build  Model
    model = LGBMClassifier(boosting_type='gbdt',num_iteration=500)
    model.fit(train, y)
    # save the model to disk
    pickle.dump(model, open(filename, 'wb'))
else:
    # load the model from disk
    model = pickle.load(open(filename, 'rb'))

if st.sidebar.button("Prediction"):
    prediction = model.predict_proba(test)[0]
    st.header('Fraud Detection Predictions')
    label = "Fraud" if prediction[0] > 0.5 else "Non-Fraud"
    probabilty = prediction[0] if label == "Fraud" else prediction[1]
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{probabilty:.3f}**')
else:
    st.warning("Please Click on Prediction")
st.write('---')
