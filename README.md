# Streamlit App For Customer Churn Prediction Using Embedded Machine Learning Model.
The Customer Churn Prediction App is designed to help businesses in the telecommunications industry predict whether a customer is likely to churn (leave the service). By leveraging machine learning techniques, this app provides valuable insights into customer behavior, allowing companies to take proactive measures to improve customer retention.

I used python for this project.
## What is streamlit?
Streamlit is a free Python library designed for quickly building attractive and interactive web applications. Its growing popularity among data scientists stems from its straightforward and user-friendly nature.

## Problem Objective & Machine Learning Formulation.
As described in the objective, the objective is to Configure Streamlit in environment and create a User Interface for regression model from (https://github.com/alicembera/Telco-Customer-Churn-Prediction). The best-performing model of the analysis was used for the Streamlit app.

My app has the following pages app:
## Home page. 
Our home page has information about the application including the main objective, key features, how its works and the benefits.

## Data page.
This page should display the data found in the database shared for this project.

## Dashboard page.
We Created an interactive dashboard to visualize the data from the database with meaningful insights. Our dashboard page show the visualization based on our analysis. We made it by using data from the data page. And we already have 2 types of dashboard which is:

- An EDA dashboard
- A KPIs Dashboard

## Predict page.
Here we interact with the Machine Learning model to make predictions. Predictions was also include probabilities of accuracy.

## History page.
This page comes to show a dataframe with the previous predictions made and values entered by users showing as a dataframe. And also the time were made and the predicted value including the original input.

In building this Streamlit app, the team followed the process of;

1. Importing the necessary libraries
2. Loading the trained model and encoder
3. Defining the input and output interfaces for the app
4. Lastly, the prediction function was defined by preprocessing user inputs, using the encoder and feeding them into the trained model to facilitate the prediction.

## Conclusion.
Clearly, creating a basic app with Python and Streamlit is both straightforward and enjoyable. This can serve as a foundation for developing more sophisticated applications down the line. So, take the plunge and begin crafting your own app today!

### Thank you!

Link to article on medium: https://medium.com/@mberaalice7/streamlit-app-for-customer-churn-prediction-using-embedded-machine-learning-model-b278626a48b3

Link to deployed app: https://embedded-machine-learning-model.onrender.com/


## Author.
Alice Mbera






