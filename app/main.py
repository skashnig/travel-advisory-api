from fastapi import FastAPI
app = FastAPI()
import requests
import os
from dotenv import load_dotenv

load_dotenv()

openweather_key = os.getenv("OPENWEATHER_API_KEY")
news_key = os.getenv("NEWS_API_KEY")

@app.get("/advisory/{country_code}")
def get_advisory(country_code: str):

    # Get geolocation data for the country from the country code
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={country_code}&appid={openweather_key}")
    data = response.json()
    print(f"Geo response status: {response.status_code}")
    print(f"Geo response data: {data}")
    print(data)
    #lat = data[0]["lat"]
    #lon = data[0]["lon"]
    lat = 40.7128
    lon = -74.0060

    # Get weather data for the location from the lat and lon
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={openweather_key}")
    weather_data = weather_response.json()
    #print(weather_data)
    #weather = weather_data["current"]
    weather = "Sunny"

    # Get news data for the country from the country code
    news_response = requests.get(f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={news_key}")
    news_data = news_response.json()
    print(news_data)
    travel_warning = []
    for article in news_data["articles"]:
        travel_warning.append(article["title"])

    return {"country_code": country_code, "travel_warning": travel_warning, "weather": f"{weather}"}
