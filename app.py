import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl', 'rb'))

st.header('Car Price Prediction ML model')


cars_data = pd.read_csv('car_price_dataset.csv')

# def get_brand_name(car_name):
#     car_name = car_name.split(' ')[0]
#     return car_name.strip()
cars_data['Brand'] = cars_data['Brand']


Brand = st.selectbox("Brand", ['Kia',  'Chevrolet' ,'Mercedes', 'Audi' ,'Volkswagen', 'Toyota' ,'Honda', 'BMW',
 'Hyundai' ,'Ford']) 
Model = st.selectbox("Model",['Rio', 'Malibu', 'GLA', 'Q5', 'Golf' ,'Camry', 'Civic' ,'Sportage' ,'RAV4',
    '5 Series', 'CR-V', 'Elantra', 'Tiguan', 'Equinox', 'Explorer' ,'A3' ,'3 Series',
    'Tucson', 'Passat' ,'Impala', 'Corolla' ,'Optima' ,'Fiesta', 'A4' ,'Focus',
    'E-Class' ,'Sonata', 'C-Class' ,'X5', 'Accord'] )
Year = st.number_input("Year", min_value=1990, max_value=2025, step=1)
Engine_Size = st.number_input("Engine Size (L)", min_value=0.5, max_value=10.0, step=0.1)
Fuel_Type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
Transmission = st.selectbox("Transmission", ['Manual', 'Automatic', 'Semi-Automatic'])
Mileage = st.number_input("Mileage (miles)", min_value=0)
Owner_Count = st.number_input("Number of Previous Owners", min_value=0, max_value=5, step=1)


if st.button("Predict"):
    input_data_model = pd.DataFrame([[Brand,Model,Year,Engine_Size,Fuel_Type,Transmission,Mileage,	Owner_Count]], columns=['Brand', 'Model', 'Year', 'Engine_Size', 'Fuel_Type', 'Transmission', 'Mileage', 'Owner_Count'])
    
    input_data_model['Owner_Count'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],
                           [1,2,3,4,5], inplace=True)
    input_data_model['Fuel_Type'].replace(['Diesel' ,'Hybrid' ,'Electric', 'Petrol'], [1, 2, 3, 4], inplace=True)
    input_data_model['Model'].replace(['Rio', 'Malibu', 'GLA', 'Q5', 'Golf' ,'Camry', 'Civic' ,'Sportage' ,'RAV4',
    '5 Series', 'CR-V', 'Elantra', 'Tiguan', 'Equinox', 'Explorer' ,'A3' ,'3 Series',
    'Tucson', 'Passat' ,'Impala', 'Corolla' ,'Optima' ,'Fiesta', 'A4' ,'Focus',
    'E-Class' ,'Sonata', 'C-Class' ,'X5', 'Accord'], [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], inplace=True)
    input_data_model['Transmission'].replace(['Manual', 'Automatic', 'Semi-Automatic'], [1, 2, 3], inplace=True)
    input_data_model['Brand'].replace(
    ['Kia', 'Chevrolet', 'Mercedes', 'Audi', 'Volkswagen', 'Toyota', 'Honda', 'BMW', 'Hyundai', 'Ford'],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], inplace=True)


    car_price = model.predict(input_data_model)

    st.markdown('Car Price is going to be '+ str(car_price[0]))

