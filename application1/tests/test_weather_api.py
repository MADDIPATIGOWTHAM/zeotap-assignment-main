import pytest
from api.weather_api import fetch_weather_data
from config import API_KEY

def test_api_connection():
    response = fetch_weather_data("Delhi")
    assert response['cod'] == 200  # Check for successful response
