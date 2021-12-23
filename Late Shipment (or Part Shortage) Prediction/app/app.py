import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Late Shipment Prediction App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Late Shipment Prediction')
st.sidebar.write('---')

st.write("""
# Late Shipment (or Part Shortage) Prediction App

This app predicts the **Late Shipments**!
""")
st.write('---')

# Load Dataset
data_path = 'late_shipment_data.csv'
data_df = pd.read_csv(data_path, encoding = 'ISO-8859-1')
data_df = data_df.drop(['Vendor INCO Term', 'Brand', 'Dosage', 'Dosage Form', 'Product Group', 'Sub Classification', 'ID', 'Managed By', 'Item Description', 'Molecule/Test Type', 'Manufacturing Site', 'First Line Designation', 'Line Item Insurance (USD)'], axis=1)
data_df = data_df[data_df['Weight (Kilograms)'].notna()]
data_df = data_df[data_df['Freight Cost (USD)'].notna()]
data_df = data_df[data_df['Shipment Mode'].notna()]
cols = {'Unit of Measure (Per Pack)': 'Unit_of_Measure_Per_Pack', 'Line Item Quantity': 'Line_Item_Quantity',
  'Line Item Value': 'Line_Item_Value', 'Pack Price': 'Pack_Price', 'Unit Price': 'Unit_Price', 
  'Weight (Kilograms)': 'Weight_in_Kilograms', 'Freight Cost (USD)': 'Freight_Cost_in_USD', 
  'Fulfill Via': 'Fulfill_Via', 'Shipment Mode': 'Shipment_Mode'
}
data_df = data_df.rename(columns=cols)
st.write(data_df.head(20))

# showing fig1
st.subheader('% of Late Delivery by Transportation Method')
df1 = data_df.where(data_df['Late_delivery'] == 1).groupby('Shipment_Mode').agg({'Late_delivery': 'count'})
df2 = data_df.where(data_df['Late_delivery'] == 0).groupby('Shipment_Mode').agg({'Late_delivery': 'count'})
df_perc = (df1/(df2+df1))
fig = px.bar(df_perc, y='Late_delivery')
fig.update_yaxes(title_text = 'Late Delivery')
fig.update_xaxes(tickangle = 0, title_text = 'Shipment Mode')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside', marker=dict(color='MediumPurple'))
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('% of Late Delivery by Fulfillment (RDC = Regional Drop Center)')
df1 = data_df.where(data_df['Late_delivery'] == 1).groupby('Fulfill_Via').agg({'Late_delivery': 'count'})
df2 = data_df.where(data_df['Late_delivery'] == 0).groupby('Fulfill_Via').agg({'Late_delivery': 'count'})
df_perc = (df1/(df2+df1))
fig = px.bar(df_perc, y='Late_delivery')
fig.update_yaxes(title_text = 'Late Delivery')
fig.update_xaxes(tickangle = 0, title_text = 'Fulfill Via')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside', marker=dict(color='magenta'))
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig3
st.subheader('% of Late Delivery by Vendor')
df1 = data_df.where(data_df['Late_delivery'] == 1).groupby('Vendor').agg({'Late_delivery': 'count'})
df2 = data_df.where(data_df['Late_delivery'] == 0).groupby('Vendor').agg({'Late_delivery': 'count'})
df_perc = (df1/(df2+df1))
fig = px.bar(df_perc, y='Late_delivery')
fig.update_yaxes(title_text = 'Late Delivery')
fig.update_xaxes(tickangle = 45)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig4
st.subheader('Late Delivery By Destination')
df1 = data_df.where(data_df['Late_delivery'] == 1).groupby('Country').agg({'Late_delivery': 'count'})
df2 = data_df.where(data_df['Late_delivery'] == 0).groupby('Country').agg({'Late_delivery': 'count'})
df_perc = (df1/(df2+df1))
fig = px.bar(df_perc, y='Late_delivery')
fig.update_yaxes(title_text = 'Late Delivery')
fig.update_xaxes(tickangle = 45)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside', marker=dict(color='LightSeaGreen'))
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    
    Unit_of_Measure_Per_Pack = st.sidebar.number_input('Unit of Measure (Per Pack)', 1, 1000, 78)
    Line_Item_Quantity = st.sidebar.number_input('The amount of item that was ordered', 1, 619000, 18332)
    Line_Item_Value= st.sidebar.number_input('The unit price of the line item ordered', 0, 5951900, 157600)
    Shipment_Mode= st.sidebar.selectbox('The mode of transport for part delivery', options=['Air', 'Truck', 'Air Charter', 'Ocean'])
    Pack_Price = st.sidebar.number_input('Pack Price', 0, 1345, 22)
    Unit_Price = st.sidebar.number_input('Unit Price', 0.0, 238.0, 0.6)
    Weight_in_Kilograms = st.sidebar.number_input('Weight (Kilograms)', 0, 8577354, 3400)
    Freight_Cost_in_USD = st.sidebar.number_input('Freight Cost (USD)', 0.75, 289600.0, 11100.0)  

    data = {
      'Unit_of_Measure_Per_Pack': Unit_of_Measure_Per_Pack,
      'Line_Item_Quantity': Line_Item_Quantity,
      'Line_Item_Value': Line_Item_Value,
      'Shipment_Mode': Shipment_Mode,
      'Pack_Price': Pack_Price,
      'Unit_Price': Unit_Price,
      'Weight_in_Kilograms': Weight_in_Kilograms,
      'Freight_Cost_in_USD': Freight_Cost_in_USD,
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

data_df['Shipment_Mode'] = data_df['Shipment_Mode'].replace({'Air': 1, 'Truck': 2, 'Air Charter': 3, 'Ocean': 4})
data_df = data_df.drop(['Country', 'Vendor', 'Fulfill_Via'], axis=1)

X = data_df.drop(['Late_delivery'], axis=1)
y = data_df['Late_delivery']

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
df['Shipment_Mode'] = df['Shipment_Mode'].replace({'Air': 1, 'Truck': 2, 'Air Charter': 3, 'Ocean': 4})

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)
    
    st.header('Late Shipment Predictions')
    label = 'Late Shipment' if prediction > 0.5 else 'On Time Shipment'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')

