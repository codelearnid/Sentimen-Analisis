import pickle
import streamlit as st

# Load model
gastype = pickle.load(open('Estimasi_Konsumsi_Bahan_Bakar.sav', 'rb'))

# Title
st.title('Estimasi Konsumsi Bahan Bakar')

# Input variables
distance = st.number_input('Input Jarak Yang Ditempuh')
speed = st.number_input('Input Kecepatan')
temp_inside = st.number_input('Input Suhu Udara Dalam')
temp_outside = st.number_input('Input Suhu Udara Luar')

# Gas type selection
gas_type_options = {1: 'Petrol', 2: 'Diesel', 3: 'CNG'}  # Map numbers to gas types
gas_type = st.selectbox('Input Jenis Bahan Bakar', options=list(gas_type_options.values()))

# Convert gas type back to numerical value for prediction
gas_type_numeric = list(gas_type_options.keys())[list(gas_type_options.values()).index(gas_type)]

# Prediction button
if st.button('Estimasi Konsumsi Bahan Bakar'):
    # Predict fuel consumption
    predict = gastype.predict([[distance, speed, temp_inside, temp_outside, gas_type_numeric]])
    st.write('Estimasi Konsumsi Bahan Bakar : ', predict)
