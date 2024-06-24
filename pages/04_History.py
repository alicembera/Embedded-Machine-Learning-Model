import streamlit as st
import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


# Set page configuration
st.set_page_config(page_title="History", layout="wide")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status,username = authenticator.login(location='sidebar')


if st.session_state['authentication_status']:
    authenticator.logout(location='sidebar')


    def display_history_prediction():

        csv_path = "Data/history.csv"
        csv_exists = os.path.exists(csv_path)

        if csv_exists:
            history = pd.read_csv(csv_path)
            st.dataframe(history)


    if __name__ == '__main__':

        display_history_prediction()
        st.title('History Page')

elif st.session_state['authentication_status'] is False:
    st.error('Wrong username/password')
elif st.session_state['authentication_status'] is None:
    st.info('Login to get access to the app')
    st.code("""
    Test Account
    Username: Mbera
    Password: Mberamuka@12
    """)

# st.write(st.session_state)