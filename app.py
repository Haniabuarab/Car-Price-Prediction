import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('rf_model.pkl', 'rb'))

st.title("Car Price Prediction")
st.subheader("Enter the car details here: ")

Year = st.text_input("Year the car is bought:")
Present_Price = st.text_input("Showroom price of the car (In lakhs):")
Kms_Driven = st.text_input("Car kms driven:")
Owner = st.selectbox("No of previous owners of the car: ", [0, 1, 3])
Fuel_Type_Petrol = st.selectbox("Fuel Type:", ["Petrol", "Diesel", "CNG"])
Seller_Type_Individual = st.radio("Are you a dealer or individual?", ["Individual", 'Dealer'])
Transmission_Manual = st.radio("Transmission Type: ", ["Manual", 'Automatic'])

if st.button("Calculate the selling price"):
    Present_Price = float(Present_Price)
    Kms_Driven = int(Kms_Driven)
    Kms_Driven = np.log(Kms_Driven)
    Owner = int(Owner)
    No_of_years = 2023 - int(Year)
    Fuel_Type_Diesel = 0
    if Fuel_Type_Petrol == 'Petrol':
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    if Fuel_Type_Petrol == 'Diesel':
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    if Fuel_Type_Petrol == 'CNG':
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 0
    if Seller_Type_Individual == 'Individual':
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0
    if Transmission_Manual == "Manual":
        Transmission_Manual = 1
    else:
        Transmission_Manual = 0

    prediction = model.predict([[Present_Price, Kms_Driven, Owner, No_of_years, Fuel_Type_Diesel, Fuel_Type_Petrol,
                                 Seller_Type_Individual, Transmission_Manual]])
    output = round(prediction[0], 2)
    if output < 0:
        st.text("Sorry you cannot sell this car")
    else:
        st.text("You Can Sell The Car at {}".format(output))
