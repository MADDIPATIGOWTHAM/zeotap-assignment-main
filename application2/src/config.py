import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
CITIES = ['Bangalore', 'Jabalpur', 'Noida', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # 5 minutes in seconds
TEMP_THRESHOLD = 35  # Celsius
ALERT_EMAIL = 'shobhitsoni2001@gmail.com'

# Create directories for storing data and logs if they don't exist
os.makedirs('data', exist_ok=True)
os.makedirs('logs', exist_ok=True)
