import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects  as go
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Steel Plate Fault Prediction App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Steel Plate Fault Prediction')
st.sidebar.write('---')

st.write("""
# Steel Plate Fault Prediction App

This app Predicts **Whether a Steel Plate is Faulty or Note**!
""")
st.write('---')

# Loads Dataset
data_path = 'steel_plates_fault.csv'
data_df = pd.read_csv(data_path, encoding = 'ISO-8859-1')
st.write(data_df.head(20))

# showing fig1
st.subheader('Proporation of Faulty Steel Plates')
total_count_df = data_df.groupby('Fault').size().reset_index(name='counts')
labels = 'Faulty', 'Not Faulty'
sizes = [data_df.Fault[data_df['Fault']==1].count(), data_df.Fault[data_df['Fault']==0].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.1, 0, 0])])
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('Count by Steel Plate Thickness')
df = data_df.groupby('Steel_Plate_Thickness').size().reset_index(name='counts')
fig = px.bar(data_frame=df, x='Steel_Plate_Thickness', y='counts', barmode='group')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
fig.update_xaxes(title='Steel Plate Thickness')
st.plotly_chart(fig, use_container_width=False)

# showing fig3  
st.subheader('% of Type of Steel Plates')
labels = 'A300', 'A400'
sizes = [data_df.TypeOfSteel_A300[data_df['TypeOfSteel_A300']==1].count(), data_df.TypeOfSteel_A400[data_df['TypeOfSteel_A400']==0].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
fig.update_traces(marker=dict(colors=['darkblue', 'cyan']))
st.plotly_chart(fig, use_container_width=False)

def user_input_features():

    X_Minimum = st.sidebar.number_input('X Minimum', 0, 1705, 447)
    X_Maximum = st.sidebar.number_input('X Maximum', 4, 1713, 481)
    Y_Minimum = st.sidebar.number_input('Y Minimum', 6712, 12987661, 1633742)
    Y_Maximum = st.sidebar.number_input('Y Maximum', 6724, 12987692, 1633742)
    Pixels_Areas = st.sidebar.number_input('Pixels Area', 2, 152655, 1884)
    X_Perimeter = st.sidebar.number_input('X Perimeter', 2, 10449, 111)
    Y_Perimeter = st.sidebar.number_input('Y Perimeter', 1, 18152, 83)
    Sum_of_Luminosity = st.sidebar.number_input('Sum of Luminosity', 250, 11591414, 205305)
    Minimum_of_Luminosity = st.sidebar.number_input('Minimum of Luminosity', 0, 203, 85)
    Maximum_of_Luminosity = st.sidebar.number_input('Maximum of Luminosity', 37, 253, 130)
    Length_of_Conveyer = st.sidebar.number_input('Length of Conveyer', 1227, 1794, 1459)
    TypeOfSteel = st.sidebar.selectbox('Type Of Steel', options=['A300', 'A400'])
    TypeOfSteel_A300, TypeOfSteel_A400 = (1, 0) if TypeOfSteel == 'A300' else (0, 1)
    Steel_Plate_Thickness = st.sidebar.number_input('Steel Plate Thickness', 40, 300, 78)
    Edges_Index = st.sidebar.number_input('Edges Index', 0.0000, 1.0000, 0.3346)
    Empty_Index = st.sidebar.number_input('Empty Index', 0.0000, 0.9439, 0.4118)
    Square_Index = st.sidebar.number_input('Square Index', 0.0083, 1.0000, 0.5718)
    Outside_X_Index = st.sidebar.number_input('Outside X Index', 0.0015, 0.8759, 0.0330)
    Edges_X_Index = st.sidebar.number_input('Edges X Index', 0.0144, 1.0000, 0.6125)
    Edges_Y_Index = st.sidebar.number_input('Edges Y Index', 0.0484, 1.0000, 0.8158)
    Outside_Global_Index = st.sidebar.select_slider('Outside Global Index', options=[0.0, 1.0, 0.5])
    LogOfAreas = st.sidebar.number_input('Log Of Areas', 0.3010, 5.1837, 2.4863)
    Log_X_Index = st.sidebar.number_input('Log X Index', 0.3010, 3.0741, 1.3316)
    Log_Y_Index = st.sidebar.number_input('Log Y Index', 0.0000, 4.2587, 1.3994)
    Orientation_Index = st.sidebar.number_input('Orientation Index', -0.9910, 0.9917, 0.0842)
    Luminosity_Index = st.sidebar.number_input('Luminosity Index', -0.9989, 0.6421, -0.1294)
    SigmoidOfAreas = st.sidebar.number_input('Sigmoid Of Areas', 0.1190, 1.0000, 0.5829)

    data = {
        'X_Minimum': X_Minimum, 
        'X_Maximum': X_Maximum, 
        'Y_Minimum': Y_Minimum, 
        'Y_Maximum': Y_Maximum, 
        'Pixels_Areas': Pixels_Areas,
        'X_Perimeter': X_Perimeter, 
        'Y_Perimeter': Y_Perimeter, 
        'Sum_of_Luminosity': Sum_of_Luminosity,
        'Minimum_of_Luminosity': Minimum_of_Luminosity, 
        'Maximum_of_Luminosity': Maximum_of_Luminosity, 
        'Length_of_Conveyer': Length_of_Conveyer,
        'TypeOfSteel_A300': TypeOfSteel_A300, 
        'TypeOfSteel_A400': TypeOfSteel_A400, 
        'Steel_Plate_Thickness': Steel_Plate_Thickness,
        'Edges_Index': Edges_Index, 
        'Empty_Index': Empty_Index, 
        'Square_Index': Square_Index, 
        'Outside_X_Index': Outside_X_Index,
        'Edges_X_Index': Edges_X_Index, 
        'Edges_Y_Index': Edges_Y_Index, 
        'Outside_Global_Index': Outside_Global_Index, 
        'LogOfAreas': LogOfAreas,
        'Log_X_Index': Log_X_Index, 
        'Log_Y_Index': Log_Y_Index, 
        'Orientation_Index': Orientation_Index, 
        'Luminosity_Index': Luminosity_Index,
        'SigmoidOfAreas': SigmoidOfAreas,
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

X = data_df.drop(['Fault'], axis=1)
y = data_df['Fault']

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

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Steel Plabe Fault Intelligence Predictions')
    label = 'Faulty' if prediction > 0.5 else 'Not Faulty'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')
