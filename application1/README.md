**Weather Tracker Application**


**Overview**
The Weather Tracker Application is designed to provide real-time weather updates and alerts based on user-defined thresholds. It stores historical weather data and visualizes trends, making it a useful tool for monitoring weather conditions across various cities.

**Table of Contents:-**

->Features

->Design Choices

->Requirements

->Setup Instructions

->Running the Application

**Features:-**

->Fetches weather data from an external API.

->Sends email alerts based on temperature thresholds.

->Stores temperature data in Firebase Realtime Database.

->Visualizes daily summaries and historical trends using Matplotlib.

**Design Choices:-**

->Modular Architecture: The application is structured into modules for fetching, processing, alerting, and visualizing data.

->Firebase: Chosen for its real-time capabilities, allowing seamless updates and retrieval of weather data.

->Email Notifications: Implemented via SMTP for timely alerts on weather conditions.

**Requirements:-**

->Dependencies

->Python 3.8 or higher

->firebase-admin

->matplotlib

->pandas

->requests

->tkinter (included with standard Python installations)

->Setup Instructions

**Clone the Repository:-**

bash:

Copy code

git clone <repository-url>

cd weather-tracker

**Create a Virtual Environment:-**

bash:

Copy code

python -m venv .venv

Activate the Virtual Environment

**Windows:**

bash

Copy code

.venv\Scripts\activate

**macOS/Linux:**

bash

Copy code

source .venv/bin/activate

Install Dependencies

**Create a requirements.txt file with the following content:**

plaintext

Copy code

firebase-admin

matplotlib

pandas

requests

**Install the dependencies:**

bash

Copy code

pip install -r requirements.txt

**Firebase Setup:-**

Create a Firebase project in the Firebase Console.

Add a Realtime Database to your project.

Download the service account JSON file and place it in the storage directory of your project.

Update the database URL in database.py to match your Firebase project's URL.

Configure Email Notifications

**NOTE:**

Update the email configuration in alerts.py with your email address and SMTP server settings. Use an App Password for Gmail if two-factor authentication is enabled.
