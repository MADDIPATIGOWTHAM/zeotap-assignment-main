import smtplib
from email.mime.text import MIMEText
import os
from config import THRESHOLDS

consecutive_breach_count = 0

def send_email(alert_message):
    sender_email = "<FROM>"
    receiver_email = "<TO>"
    subject = "Weather Alert"

    msg = MIMEText(alert_message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, os.getenv('PASSWORD'))  # Use an environment variable for the password
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def check_alerts(weather):
    global consecutive_breach_count
    alerts = []
    
    temp = weather['main']['temp']
    main_condition = weather['weather'][0]['main']

    if temp > THRESHOLDS['temperature']:
        consecutive_breach_count += 1
        if consecutive_breach_count == THRESHOLDS['consecutive_updates']:
            alert_message = f"Alert: High temperature of {temp}°C!"
            alerts.append(alert_message)
            send_email(alert_message)
    else:
        consecutive_breach_count = 0

    if main_condition == THRESHOLDS['condition']:
        alert_message = f"Alert: Current weather condition is {main_condition}!"
        alerts.append(alert_message)
        send_email(alert_message)

    return alerts
