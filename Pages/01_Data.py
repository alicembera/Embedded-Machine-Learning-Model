import streamlit as st
import pandas as pd
import os


def filter_columns(data):
    # Allow the user to select the data type to display
    data_type = st.selectbox('Select Data type', [
                             'All', 'Numeric Columns', 'Categorical Columns'])

    if data_type == 'Numeric Columns':
        data = data.select_dtypes(include=['number'])
    elif data_type == 'Categorical Columns':
        data = data.select_dtypes(include=['object', 'category'])

    # Display the filtered data in Streamlit
    st.write('Filtered Data:', data)


# Define the path to the dataset
dataset_path = 'Data/train.csv'

# Check if the file exists
if not os.path.isfile(dataset_path):
    st.error(
        f"The file '{dataset_path}' does not exist. Please check the path.")
else:
    try:
        # Load the dataset
        data = pd.read_csv(dataset_path)
        # st.write('Loaded Data:', data)
        # Call the function to filter and display columns
        filter_columns(data)
    except Exception as e:
        st.error(f"Error loading the file '{dataset_path}': {e}")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        # st.write('Loaded Data:', data)
        # Call the function to filter and display columns
        filter_columns(data)
    except Exception as e:
        st.error(f"Error loading the uploaded file: {e}")


# # Define the path to the dataset
# dataset_path = 'Data/train.csv'

# # Check if the file exists
# if not os.path.isfile(dataset_path):
#     st.error(f"The file '{dataset_path}' does not exist. Please check the path.")
# else:
#     try:
#         # Load the dataset
#         data = pd.read_csv(dataset_path)
#         st.write('Loaded Data:', data)
#     except Exception as e:
#         st.error(f"Error loading the file '{dataset_path}': {e}")

# # File uploader
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     try:
#         data = pd.read_csv(uploaded_file)

#         # Allow the user to select data type to display
#         data_type = st.selectbox('Select Data type', ['All', 'Numeric Columns', 'Categorical Columns'])

#         if data_type == 'Numeric Columns':
#             filtered_data = data.select_dtypes(include=['number'])
#         elif data_type == 'Categorical Columns':
#             filtered_data = data.select_dtypes(include=['object'])
#         else:
#             filtered_data = data

#         # Display the filtered data in Streamlit
#         st.write('Loaded Data:', filtered_data)
#     except Exception as e:
#         st.error(f"Error loading the uploaded file: {e}")
