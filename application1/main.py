import time
import pandas as pd
import matplotlib.pyplot as plt
from api.weather_api import fetch_weather_data
from processing.data_processing import process_weather_data
from processing.alerts import check_alerts
from config import API_KEY
from visualization.plots import plot_daily_summary
from storage.database import initialize_firebase, store_temperature, fetch_historical_data
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad", "Bhimavaram"]

def fetch_and_store_weather(city):
    daily_temps = {}
    try:
        weather = fetch_weather_data(city)
        process_weather_data(weather)
        alerts = check_alerts(weather)

        if alerts:
            for alert in alerts:
                print(alert)

        temperature = weather['main']['temp']
        daily_temps[city] = temperature

        # Store temperature in Firebase
        store_temperature(city, temperature)

    except Exception as e:
        print(f"Error fetching weather data for {city}: {e}")

    return daily_temps

def create_summary(daily_temps, summary):
    current_date = time.strftime("%Y-%m-%d")
    for city in CITIES:
        if city not in summary['avg_temps']:
            summary['avg_temps'][city] = []
        summary['avg_temps'][city].append(daily_temps.get(city, 0))
    summary['dates'].append(current_date)

def visualize_historical_data(city):
    historical_data = fetch_historical_data(city)
    if historical_data:
        df = pd.DataFrame(historical_data, columns=['timestamp', 'temperature'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='s')
        plt.figure(figsize=(10, 5))
        plt.plot(df['date'], df['temperature'], marker='o')
        plt.title(f'Historical Temperature Trends for {city}')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()
    else:
        print(f"No historical data found for {city}.")

def start_weather_updates(city):
    initialize_firebase()
    summary = {
        "dates": [],
        "avg_temps": {}
    }

    daily_temps = fetch_and_store_weather(city)
    create_summary(daily_temps, summary)

    print("Daily Summary for", city, ":", summary)
    plot_daily_summary(summary)

def create_gui():
    root = tk.Tk()
    root.title("Weather Tracker")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    city_label = tk.Label(frame, text="Enter City:")
    city_label.pack(pady=5)

    city_entry = tk.Entry(frame)
    city_entry.pack(pady=5)

    def start_updates():
        city = city_entry.get()
        if city:
            start_weather_updates(city)
        else:
            messagebox.showwarning("Input Error", "Please enter a city name.")

    start_button = tk.Button(frame, text="Start Weather Updates", command=start_updates)
    start_button.pack(pady=5)

    stop_button = tk.Button(frame, text="Stop Weather Updates", command=root.quit)
    stop_button.pack(pady=5)

    def show_message():
        messagebox.showinfo("Info", "Weather updates are running.")

    info_button = tk.Button(frame, text="Show Info", command=show_message)
    info_button.pack(pady=5)

    # Picklist for showing historical data
    selected_city = StringVar(frame)
    selected_city.set(CITIES[0])  # Set default value

    city_option_menu = OptionMenu(frame, selected_city, *CITIES)
    city_option_menu.pack(pady=5)

    def show_historical_data():
        city = selected_city.get()
        visualize_historical_data(city)

    historical_button = tk.Button(frame, text="Show Historical Data", command=show_historical_data)
    historical_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
