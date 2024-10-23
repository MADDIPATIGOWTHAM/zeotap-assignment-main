# firebase_setup.py
import firebase_admin
from firebase_admin import credentials, db
import time
from firebase_admin import db
import pandas as pd
def initialize_firebase():
    cred = credentials.Certificate("C:/Users/ganesh/OneDrive/Desktop/zeotap/storage/serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://zeotap-bebbe-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
def store_temperature(city, temperature):
    ref = db.reference('temperatures')
    
    # Fetch existing data for the city
    existing_data = ref.order_by_child('city').equal_to(city).get()
    
    timestamp = int(time.time())  # Get current timestamp in seconds

    if existing_data:
        # If the city exists, update its temperature and timestamp lists
        for key in existing_data.keys():
            current_temps = existing_data[key]['temperatures']
            current_times = existing_data[key]['timestamps']
            
            # Append new values
            current_temps.append(temperature)
            current_times.append(timestamp)
            
            # Update the database
            ref.child(key).update({
                'temperatures': current_temps,
                'timestamps': current_times
            })
    else:
        # If the city does not exist, create a new entry with lists
        ref.push({
            'city': city,
            'temperatures': [temperature],  # Initialize with the first temperature
            'timestamps': [timestamp]        # Initialize with the first timestamp
        })
def process_historical_data(historical_data):
    df = pd.DataFrame(historical_data, columns=['timestamp', 'temperature'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='s')  # Convert timestamp to datetime
    return df[['date', 'temperature']]  # Keep only relevant columns
def fetch_historical_data(city):
    ref = db.reference('temperatures')
    city_data = ref.order_by_child('city').equal_to(city).get()
    
    historical_data = []
    for key, value in city_data.items():
        for temp, timestamp in zip(value['temperatures'], value['timestamps']):
            historical_data.append((timestamp, temp))
    
    return historical_data
