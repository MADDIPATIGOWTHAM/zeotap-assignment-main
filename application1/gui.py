import tkinter as tk
from tkinter import messagebox
from api.weather_api import fetch_weather_data
from storage.database import store_temperature

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather():
    for city in CITIES:
        weather = fetch_weather_data(city)
        temperature = weather.get('main', {}).get('temp')  # Adjust based on your API response
        if temperature is not None:
            store_temperature(city, temperature)
            messagebox.showinfo("Success", f"Stored temperature for {city}: {temperature}°C")
        else:
            messagebox.showerror("Error", f"Could not fetch temperature for {city}")

def create_gui():
    root = tk.Tk()
    root.title("Weather Data Interface")

    # Fetch Weather Button
    fetch_button = tk.Button(root, text="Fetch and Store Weather Data", command=fetch_weather)
    fetch_button.pack(pady=20)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
