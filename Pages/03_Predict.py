import streamlit as st
import pandas as pd
import joblib
import os
import datetime
 
st.set_page_config(
    page_title='Predict Customer Churn!',
    page_icon='🔮',
    layout='wide'
)
 
st.title("Predict Customer Churn!")
 
# Load models and encoder
@st.cache_resource
def load_logistic_reg_pipeline():
    pipeline = joblib.load('Models/Logistic_reg.joblib')
    return pipeline
 
 
@st.cache_resource
def load_adaboost_pipeline():
    pipeline = joblib.load('Models/AdaBoost.joblib')
    return pipeline
 
 
def select_model():
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('Select a model', options=['Logistic Regression', 'AdaBoost'], key='selected_model')
    with col2:
        pass
 
    if st.session_state['selected_model'] == 'Logistic Regression':
        pipeline = load_logistic_reg_pipeline()
    else:
        pipeline = load_adaboost_pipeline()
 
    encoder = joblib.load('Models/encoder.joblib')
 
    return pipeline, encoder
 
 
 
def make_prediction(pipeline, encoder):      
    gender = st.session_state['gender']
    senior_citizen = st.session_state['senior_citizen']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    tenure = int(st.session_state['tenure'])
    paperless_billing = st.session_state['paperless_billing']
    payment_method = st.session_state['payment_method']
    monthly_charges = float(st.session_state['monthly_charges'])
    total_charges = float(st.session_state['total_charges'])
    phone_service = st.session_state['phone_service']
    multiple_lines = st.session_state['multiple_lines']
    internet_service = st.session_state['internet_service']
    online_security = st.session_state['online_security']
    online_backup = st.session_state['online_backup']
    device_protection = st.session_state['device_protection']
    tech_support = st.session_state['tech_support']
    streaming_tv = st.session_state['streaming_tv']
    streaming_movies = st.session_state['streaming_movies']
    contract = st.session_state['contract']
    probability = st.session_state['probability']
    prediction = st.session_state['prediction']
   
    data = {'gender': [gender], 'seniorcitizen': [senior_citizen], 'partner': [partner], 'dependents': [dependents],
        'tenure': [tenure], 'paperlessbilling': [paperless_billing],'paymentmethod': [payment_method], 'monthlycharges': [monthly_charges],
        'totalcharges': [total_charges], 'phoneservice': [phone_service], 'multiplelines': [multiple_lines], 'internetservice': [internet_service],
       'onlinesecurity': [online_security], 'onlinebackup': [online_backup], 'deviceprotection': [device_protection], 'techsupport': [tech_support],
       'streamingtv': [streaming_tv], 'streamingmovies': [streaming_movies], 'contract': [contract] }
   
    # Make a DataFrame
    df = pd.DataFrame(data)
 

    # st.write(pipeline)
    # st.write(st.session_state)
    # # info = df.info()
    # st.write(info)
   
 
    # Define Probability and Prediction
    pred = pipeline.predict(df)
    pred_int = int(pred[0])
    prediction = encoder.inverse_transform([pred_int])[0]
    probability = pipeline.predict_proba(df)[0][pred_int]*100
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability
   
    df['prediction'] = prediction
    df['probability'] = probability
    df['time_of_prediction'] = datetime.date.today()
    df['model_used'] = st.session_state['selected_model']

    df.to_csv("Data/history.csv", mode='a', header=not os.path.exists("Data/history.csv"))

    return prediction, probability
 
if 'prediction' not in st.session_state:
    st.session_state['prediction']= None
if 'probability' not in st.session_state:
    st.session_state['probability']= None
 
 
# Creating the form
def display_form():
 
    pipeline, encoder = select_model()
 
    with st.form('input_features'):
 
        col1, col2 = st.columns(2)
        with col1:
            st.write('### Customer Demographics')
            gender = st.selectbox('Gender', options = ['Male', 'Female'], key = 'gender')
            senior_citizen = st.selectbox('Senior Citizen', options = ['1', '0'], key = 'senior_citizen')
            partner = st.selectbox('Partner', options = ['Yes', 'No'], key = 'partner')
            dependents = st.selectbox('dependents', options= ['Yes', 'No'], key = 'dependents')
            tenure = st.number_input('Tenure (months)', min_value=0, max_value=100, step=1, key = 'tenure')
            st.write('### Billing and Payment')
            paperless_billing = st.selectbox('Paperless Billing', options = ['Yes', 'No'], key = 'paperless_billing')
            payment_method = st.selectbox('Payment Method', options = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key = 'payment_method')
            monthly_charges = st.number_input('Monthly Charges ($)', min_value=0.0, format="%.2f",step = 1.00, key = 'monthly_charges')
            total_charges = st.number_input('Total Charges ($)', min_value=0.0, format="%.2f", step=1.00, key = 'total_charges')
        with col2:
            st.write('### Services Subscribed')
            phone_service = st.selectbox('Phone Service', options = ['Yes', 'No'], key = 'phone_service')
            multiple_lines = st.selectbox('Multiple Lines', options = ['Yes', 'No'], key = 'multiple_lines')
            internet_service = st.selectbox('Internet Service', options = ['DSL', 'Fiber optic', 'No'], key = 'internet_service')
            online_security = st.selectbox('Online Security', options = ['Yes', 'No'], key = 'online_security')
            online_backup = st.selectbox('Online Backup', options = ['Yes', 'No'], key = 'online_backup')
            device_protection = st.selectbox('Device Protection', options = ['Yes', 'No'], key = 'device_protection')
            tech_support = st.selectbox('Tech Support', options = ['Yes', 'No'], key = 'tech_support')
            streaming_tv = st.selectbox('Streaming TV', options = ['Yes', 'No'],  key = 'streaming_tv')
            streaming_movies = st.selectbox('Streaming Movies', options = ['Yes', 'No'], key = 'streaming_movies')
            contract = st.selectbox('Contract', options = ['Month-to-month', 'One year', 'Two year'], key = 'contract')
           
        st.form_submit_button('Submit', on_click=make_prediction, kwargs = dict(pipeline = pipeline, encoder = encoder))
 
 
 
if __name__ == '__main__':
 
 
    display_form()
    final_prediction = st.session_state['prediction']
    final_probability = st.session_state['probability']
 
    if final_prediction is None:
        st.write('Predictions show here!')
        st.divider()
    else:
        if final_prediction.lower() == 'yes':
            # st.markdown(f'## Churn: {final_prediction}')
            st.markdown(f'### Customer will leave 😞.')
            st.markdown(f'## Probability: {final_probability:.2f}%')
            
        else:
            # st.markdown(f'## Churn: {final_prediction}')
            st.markdown(f'### Customer will stay 😊.')
            st.markdown(f'## Probability: {final_probability:.2f}%')
            
 
    # st.write(st.session_state)