import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import joblib



# Load the numerical imputer
#num_imputer = joblib.load("numerical_imputer.joblib")

# Load the categorical imputer
#cat_imputer = joblib.load("categorical_imputer.joblib")

# Load the scaler
#scaler = joblib.load("scaler.joblib")

# Load the label encoder for 'family' feature
#le_family = joblib.load("le_family.joblib")

# Load the label encoder for 'holiday_type' feature
#le_holiday_type = joblib.load("le_holiday_type.joblib")

# Load the label encoder for 'city' feature
#le_city = joblib.load("le_city.joblib")

# Load the final model
regressor = joblib.load("Best_model.joblib")



#@st.cache_resource()
def show_predict_page():
     # Add a title and subtitle
    st.write("<center><h1>Predicting Sales App</h1></center>", unsafe_allow_html=True)


    # Add a subtitle or description
    st.write("This app predict sales by the using machine learning, based on certain input parameters. Simply enter the required information and click 'Predict' to get a sales prediction!")

    st.subheader("Enter the following details to predict sales")

    input_data = {
        'store_nbr': st.slider("store_nbr", step=1, min_value=0, max_value=54),
        'onpromotion': st.number_input("onpromotion, 0 - 800", min_value=0, max_value=800),
        'transactions': st.number_input("Number of Transactions, 0 - 10000", min_value=0, max_value=10000),
        'oil_price': st.number_input("oil_price, 1 - 200", step=1, min_value=0, max_value=200),
        'cluster': st.slider("cluster", step=1, min_value=0, max_value=17),
        'day': st.slider("day", 1, 31, 1),
        'year': st.selectbox("year", [1970]),
        'month': st.slider("month", 1, 12, 1),
        #'dayofmonth': st.slider("dayofmonth", 1, 31, 1),
        #'dayofweek': st.slider("dayofweek, 0=Sun and 6=Sat", step=1, min_value=1, max_value=6),
        'family': st.selectbox("products", ['AUTOMOTIVE', 'Personal Care', 'Beverages', 'STATIONERY', 'Food', 'CLEANING', 'HARDWARE', 'Home and Kitchen', 'Clothing', 'PET SUPPLIES', 'ELECTRONICS']),
        'holiday_type': st.selectbox("holiday_type", ['Workday', 'holiday']),
        'city': st.selectbox("City", ['Salinas', 'Quito', 'Cayambe', 'Latacunga', 'Riobamba', 'Ibarra', 'Santo Domingo', 'Guaranda', 'Ambato', 'Guayaquil', 'Daule', 'Babahoyo', 'Quevedo', 'Playas', 'Cuenca', 'Loja', 'Machala', 'Esmeraldas', 'El Carmen', 'Libertad', 'Manta', 'Puyo'])
    }

# Create a button to make a prediction

    if st.button("Predict", key="predict_button", help="Click to make a prediction."):
        # Convert the input data to a pandas DataFrame
        input_df = pd.DataFrame([input_data])


# Selecting categorical and numerical columns separately
#        cat_columns = [col for col in input_df.columns if input_df[col].dtype == 'object']
#        num_columns = [col for col in input_df.columns if input_df[col].dtype != 'object']


# Apply the imputers
#        input_df_imputed_cat = cat_imputer.transform(input_df[cat_columns])
#        input_df_imputed_num = num_imputer.transform(input_df[num_columns])

# Convert the NumPy arrays to DataFrames
#        input_df_imputed_cat = pd.DataFrame(input_df_imputed_cat, columns=cat_columns)
#        input_df_imputed_num = pd.DataFrame(input_df_imputed_num, columns=num_columns)
        

# Scale the numerical columns
#        input_df_scaled = scaler.transform(input_df_imputed_num)
#        input_scaled_df = pd.DataFrame(input_df_scaled , columns = num_columns)

#        input_df_imputed  = pd.concat([input_df_imputed_cat, input_scaled_df], axis=1)
        
 # Encode the categorical columns
        # Encode the categorical columns
#        input_df_imputed['family'] = le_family.transform(input_df_imputed['family'])
#        input_df_imputed['holiday_type'] = le_holiday_type.transform(input_df_imputed['holiday_type'])
#        input_df_imputed['city'] = le_city.transform(input_df_imputed['city'])


        #input_encoded_df = pd.DataFrame(encoder.transform(input_df_imputed_cat))
        #input_encoded_df.columns = input_encoded_df.columns.astype(str)
        

#joining the cat encoded and num scaled
#        final_df = input_df_imputed 

# Make a prediction
        prediction = round(regressor.predict(input_df)[0], 2)


# Display the prediction
     #st.write(f"The predicted sales are: {prediction}.")

# Display the prediction
        st.subheader("Sales Prediction")
        st.write("The predicted sales for the company is:", prediction)