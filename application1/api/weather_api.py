import requests

def fetch_weather_data(city):
    api_key = " # Replace with your API key" 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()
