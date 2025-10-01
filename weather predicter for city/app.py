import streamlit as st
import requests
from config import api_key

st.title("Weather Predictor for City")
st.write("Enter the city name to get the weather prediction.")

city = st.text_input("City Name")

if st.button("Get Weather Prediction"):
    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"].title()
            wind_speed = data["wind"]["speed"]
            st.success(f"Weather for {city.title()}")
            st.write(f"Temperature: {temp}°C")
            st.write(f"Feels like: {feels_like}°C")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Weather: {weather_desc}")
            st.write(f"Wind speed: {wind_speed} m/s")
        else:
            st.error("Failed to fetch weather data. Please check the city name or API key.")
    else:
        st.warning("Please enter a city name.")
else:
    st.info("Click the button to get the weather prediction.")
    


    
