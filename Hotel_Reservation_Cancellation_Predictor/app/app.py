import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import plotly.graph_objects  as go
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Hotel Reservation Cancellation Prediction App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Hotel Reservation Cancellation Prediction')
st.sidebar.write('---')

st.write("""
# Hotel Reservation Cancellation Prediction App

This app predicts **Predict the likelihood of Guest Booking Cancellation**!
""")
st.write('---')

# load data
data_df = pd.read_csv('hotel_reservation_cancel.csv')
st.write(data_df.head(20))

# showing fig1
st.subheader('Cancellation % in Total Booking')
labels = 'Cancelled Booking', 'Booked'
sizes = [data_df.is_canceled[data_df['is_canceled']==1].count(), data_df.is_canceled[data_df['is_canceled']==0].count()]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.1, 0, 0])])
fig.update_traces(marker=dict(colors=['darkblue', 'cyan']))
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('No. of Guests visited on a Particular Day of the Month')
df = data_df.groupby('arrival_date_day_of_month').size().reset_index(name='counts')
fig = px.bar(data_frame=df, x='arrival_date_day_of_month', y='counts', barmode='group')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
fig.update_xaxes(title='Day of Month')
fig.update_yaxes(title='No. of Guests')
st.plotly_chart(fig, use_container_width=False)

# showing fig3
st.subheader('Most Cancelled Booking by Country')
fig = px.bar(data_df[data_df['is_canceled']==1].groupby('country').agg({'is_canceled': 'count'}))
fig.update_yaxes(title_text = 'Cancelled Booking')
fig.update_xaxes(tickangle = 0, title_text='Country')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
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

data_df = MultiColumnLabelEncoder(
    columns = list(data_df.select_dtypes(include=['object']).columns)
).fit_transform(data_df)

def user_input_features():
    
    hotel = st.sidebar.selectbox('Hotel', options=['Resort Hotel'])
    lead_time = st.sidebar.slider('Lead Time', 0, 737, 57)
    arrival_date = st.sidebar.date_input('Arrival Date', datetime(2015, 1, 1))
    stays_in_weekend_nights = st.sidebar.selectbox('Stays in Weekend Nights', options=[0, 1, 2, 4, 3, 6])
    stays_in_week_nights = st.sidebar.selectbox('Stays in Week Nights', options=[0, 1, 2, 3, 4, 5, 11, 8, 10, 6, 7, 15, 9])
    adults = st.sidebar.selectbox('Adults', options=[2, 1, 3, 4])
    children = st.sidebar.selectbox('Children', options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    babies = st.sidebar.selectbox('Babies', options=[0, 1, 2])
    meal = st.sidebar.selectbox('Meal', options=['BB', 'FB', 'HB'])
    country = st.sidebar.selectbox(
        'Country', 
        options=[
            'PRT', 'GBR', 'USA', 'ESP', 'IRL', 'FRA', 'ROU', 'NOR', 'OMN',
            'ARG', 'POL', 'DEU', 'BEL', 'CHE', 'CN', 'GRC', 'ITA', 'NLD',
            'DNK', 'RUS', 'SWE', 'AUS', 'EST', 'CZE', 'BRA', 'FIN', 'MOZ',
            'BWA', 'LUX', 'SVN', 'ALB', 'IND', 'CHN', 'MEX'
        ]
    )
    market_segment = st.sidebar.selectbox('Market Segment', options=['Direct', 'Corporate', 'Online TA', 'Offline TA/TO', 'Complementary', 'Groups'])
    distribution_channel = st.sidebar.selectbox('Distribution Channel', options=['Direct', 'Corporate', 'TA/TO'])
    is_repeated_guest = st.sidebar.selectbox('Is Repeated Guest', options=[0, 1])
    previous_cancellations = st.sidebar.selectbox('Previous Cancellations', options=[0, 1])
    previous_bookings_not_canceled = st.sidebar.selectbox('Previous Bookings not Canceled', options=[0, 1])
    reserved_room_type = st.sidebar.selectbox('Reserved Room Type', options=['C', 'A', 'D', 'E', 'G', 'F', 'H', 'L'])
    assigned_room_type = st.sidebar.selectbox('Assigned Room Type', options=['C', 'A', 'D', 'E', 'G', 'F', 'I', 'B', 'H'])
    booking_changes = st.sidebar.selectbox('Booking Changes', options=[3, 4, 0, 1, 2, 5])
    deposit_type = st.sidebar.selectbox('Deposit Type', options=['No Deposit'])
    days_in_waiting_list = st.sidebar.selectbox('Days in Waiting List', options=[0, 1, 2])
    customer_type = st.sidebar.selectbox('Customer Type', options=['Transient', 'Contract', 'Transient-Party', 'Group'])
    adr = st.sidebar.slider('adr', 0.0, 280.74, 132.0)
    required_car_parking_spaces = st.sidebar.selectbox('Required Car Parking Spaces', options=[1, 0, 2])
    total_of_special_requests = st.sidebar.selectbox('Total of Special Requests', options=[0, 1, 2, 3, 4])
    reservation_status_date = st.sidebar.date_input('Reservation Status Date', datetime(2015, 7, 1))

    data = {
        'hotel': hotel,
        'lead_time': lead_time,
        'arrival_date_year': arrival_date.year,
        'arrival_date_month': arrival_date.strftime('%B'),
        'arrival_date_week_number': arrival_date.isocalendar()[1],
        'arrival_date_day_of_month': arrival_date.day,
        'stays_in_weekend_nights': stays_in_weekend_nights,
        'stays_in_week_nights': stays_in_week_nights,
        'adults': adults,
        'children': children,
        'babies': babies,
        'meal': meal,
        'country': country,
        'market_segment': market_segment,
        'distribution_channel': distribution_channel,
        'is_repeated_guest': is_repeated_guest,
        'previous_cancellations': previous_cancellations,
        'previous_bookings_not_canceled': previous_bookings_not_canceled,
        'reserved_room_type': reserved_room_type,
        'assigned_room_type': assigned_room_type,
        'booking_changes': booking_changes,
        'deposit_type': deposit_type,
        'days_in_waiting_list': days_in_waiting_list,
        'customer_type': customer_type,
        'adr': adr,
        'required_car_parking_spaces': required_car_parking_spaces,
        'total_of_special_requests': total_of_special_requests,
        'reservation_status_date': reservation_status_date,
    }
    return pd.DataFrame(data, index=[0])

# Main Panel

X = data_df.drop(['is_canceled'], axis=1)
y = data_df['is_canceled']

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

df = MultiColumnLabelEncoder(
    columns = list(df.select_dtypes(include=['object']).columns)
).fit_transform(df)

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Hotel Reservation Cancellation Predictions')
    label = 'Booking Cancelled' if prediction > 0.5 else 'No Cancellation'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Probability: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')
