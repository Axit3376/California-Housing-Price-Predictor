import streamlit as st
import pandas as pd
import joblib

# Load pipeline
model = joblib.load("housing_price_pipeline.pkl")

st.title("🏘️Housing Price Predictor")

# Collect user inputs
longitude = st.number_input("Longitude", value=-120.0)
latitude = st.number_input("Latitude", value=35.0)
housing_median_age = st.number_input("Median Age", value=20)
total_rooms = st.number_input("Total Rooms", value=2000)
total_bedrooms = st.number_input("Total Bedrooms", value=400)
population = st.number_input("Population", value=800)
households = st.number_input("Households", value=300)
median_income = st.number_input("Median Income", value=3.5)
ocean_proximity = st.selectbox("Ocean Proximity",
                               ["<1H OCEAN","INLAND","NEAR OCEAN","NEAR BAY","ISLAND"])

if st.button("Predict"):
    data = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])
    price = model.predict(data)[0]
    st.success(f"Estimated Median House Price: ${price:,.0f}")