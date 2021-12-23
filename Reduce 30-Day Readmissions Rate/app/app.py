import pickle
import requests
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression


response = requests.get(url='https://katonic.ai/favicon.ico')
im = Image.open(BytesIO(response.content))

st.set_page_config(
    page_title='Reduce 30-Day Readmissions Rate App', 
    page_icon = im, 
    layout = 'wide', 
    initial_sidebar_state = 'auto'
)

st.sidebar.image('logo.png')
st.sidebar.title('Reduce 30-Day Readmissions Rate')
st.sidebar.write('---')

st.write("""
# Reduce 30-Day Readmissions Rate App

This app predicts **Which Patients are at Risk and Allowing Clinicians to Prescribe Intervention Strategies before and after the Patient is Discharged**.!
""")
st.write('---')

# Loads Dataset
data_path = 'hospital_readmission.csv'
data_df = pd.read_csv(data_path, encoding = 'ISO-8859-1')
data_df = data_df.drop(['weight', 'race', 'admission_source_id', 'gender', 'age', 'A1Cresult', 'metformin', 
'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide', 
'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 
'tolazamide', 'examide', 'citoglipton', 'insulin', 'glyburide.metformin', 'glipizide.metformin', 
'glimepiride.pioglitazone', 'metformin.rosiglitazone', 'metformin.pioglitazone', 'change', 
'max_glu_serum', 'discharge_disposition_id', 'diag_1', 'diag_2', 'diag_3', 'diag_1_desc', 'diag_2_desc', 'diag_3_desc'], axis=1)
data_df = data_df[data_df['payer_code'] != '?']
data_df = data_df[data_df['medical_specialty'] != '?']
st.write(data_df.head(20))

# showing fig1
st.subheader('Average no. of Inpatient and Outpatient Visits in the Preceding Year (True = Readmitted Patient)')
df1 = data_df.groupby('readmitted').agg({'number_inpatient': 'mean', 'number_outpatient': 'mean'})
fig = px.bar(df1)
fig.update_yaxes(title_text = 'Average no. of Inpatient and Outpatient')
fig.update_xaxes(tickangle = 0, title_text='Re-admitted')
fig.update_layout(barmode='relative', title_text='Relative Barmode')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig2
st.subheader('Probability of Readmission by Admission Type')
df1 = data_df.where(data_df['readmitted'] == 1).groupby('admission_type_id').agg({'readmitted': 'count'})
df2 = data_df.where(data_df['readmitted'] == 0).groupby('admission_type_id').agg({'readmitted': 'count'})
df_perc = (df1/(df2+df1))
fig = px.bar(df_perc, y='readmitted', color_discrete_sequence= px.colors.sequential.Redor)
fig.update_yaxes(title_text = 'Re-admitted')
fig.update_xaxes(tickangle = 0, title_text='Admission Type Id')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=False)

# showing fig3
st.subheader('No. of Diagnoses, Procedures, and Medications Per Patient (True = Readmitted Patient)')
df1 = data_df.groupby('readmitted').agg({'number_diagnoses': 'mean', 'num_lab_procedures': 'mean', 'num_medications':'mean'})
fig = px.bar(df1, color_discrete_sequence= px.colors.sequential.Cividis)
fig.update_yaxes(title_text = 'Count')
fig.update_xaxes(tickangle = 0, title_text='Re-admitted')
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

data_df = MultiColumnLabelEncoder(columns = ['payer_code', 'medical_specialty', 'diabetesMed', 'readmitted']).fit_transform(data_df)

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    
    payer_code = st.sidebar.selectbox(
        'Unique code of patient’s payer', 
        options=['CP', 'UN', 'MC', 'HM', 'SP', 'CM', 'BC', 'MD', 'WC', 'OG', 'PO', 'DM', 'SI', 'OT', 'CH']
    )
    medical_specialty = st.sidebar.selectbox(
        'Medical specialty that patient is being admitted into', 
        options=['Surgery-Neuro', 'Family/GeneralPractice', 'Psychiatry', 'Cardiology', 'InternalMedicine',
       'Surgery-Cardiovascular/Thoracic', 'Nephrology', 'Emergency/Trauma', 'Gastroenterology', 'Orthopedics',
       'Cardiology-Pediatric', 'PhysicalMedicineandRehabilitation', 'Gynecology', 'Pulmonology', 'Surgery-General', 
       'Pediatrics', 'Orthopedics-Reconstructive', 'Surgery-Pediatric', 'Otolaryngology', 'Pediatrics-CriticalCare', 
       'Hematology/Oncology', 'ObstetricsandGynecology', 'Pediatrics-Endocrinology', 'Surgery-Vascular', 'Urology', 
       'Neurology', 'Radiologist', 'Osteopath', 'Surgery-Cardiovascular', 'Psychology', 'Oncology', 'Endocrinology', 
       'OutreachServices', 'Podiatry', 'Ophthalmology', 'Hospitalist', 'Radiology', 'Obsterics&Gynecology-GynecologicOnco',
       'Surgery-Thoracic', 'Surgeon', 'Pathology', 'Surgery-Plastic', 'InfectiousDiseases', 'Anesthesiology-Pediatric', 
       'Pediatrics-Pulmonology', 'Pediatrics-Hematology-Oncology', 'Hematology', 'Surgery-Colon&Rectal', 'Surgery-PlasticwithinHeadandNeck', 
       'Pediatrics-EmergencyMedicine', 'Obstetrics', 'PhysicianNotFound']
    )
    diabetesMed = st.sidebar.selectbox('Diabetes Medication', options=['No', 'Yes'])
    time_in_hospital = st.sidebar.slider('Length of stay in hospital (Days)', 1, 14, 3)
    num_lab_procedures = st.sidebar.slider('Total lab procedures in the past', 1, 113, 65)
    num_procedures = st.sidebar.slider('Total procedures in the past', 0, 6, 2)
    num_medications = st.sidebar.slider('Total number of medications prescribed to the patient', 0, 81, 15)
    number_outpatient = st.sidebar.slider('Total outpatient visits in the past', 0, 14, 10)
    number_emergency = st.sidebar.slider('Total emergency room visits in the past',  0, 42, 10)
    number_inpatient = st.sidebar.slider('Total inpatient visits in the past',  0, 9, 5)
    number_diagnoses = st.sidebar.slider('Total diagnosis', 1, 9, 6)

    data = {
      'payer_code': payer_code,
      'medical_specialty': medical_specialty,
      'diabetesMed': diabetesMed,
      'time_in_hospital': time_in_hospital,
      'num_lab_procedures': num_lab_procedures,
      'num_procedures': num_procedures,
      'num_medications': num_medications,
      'number_outpatient': number_outpatient,
      'number_emergency': number_emergency,
      'number_inpatient': number_inpatient,
      'number_diagnoses': number_diagnoses
    }
    return pd.DataFrame(data, index=[0])

# Main Panel
data_df = data_df.drop(['admission_type_id'], axis=1)
X = data_df.drop(['readmitted'], axis=1)
y = data_df['readmitted']

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

df = MultiColumnLabelEncoder(columns = ['payer_code', 'medical_specialty', 'diabetesMed']).fit_transform(df)

# Apply Model to Make Prediction
if st.sidebar.button('Prediction'):
    prediction = model.predict(df)

    st.header('Hospital Readmission Intelligence Predictions')
    label = 'Patient At Risk'  if prediction > 0.5 else 'Patient condition is Normal'
    st.write(f'Prediction Label: **{label}**')
    st.write(f'Prediction Score: **{prediction}**')
else:
    st.warning('Please Click on Prediction')
st.write('---')

