# write a  program which reminds you to drink water every hour or two . by sending desktop notifications.
import time
from plyer import notification

INTERVAL_HOURS = 1 

def send_water_reminder():
    notification.notify(
        title="Drink Water Reminder",
        message="Time to take a break and sip a glass of water!",
        app_name="Hydration Helper",
        timeout=10  
    )

if __name__ == "__main__":
    print("Hydration Helper started! Press Ctrl+C to stop.")
    interval_seconds = INTERVAL_HOURS * 3600
    
    try:
        while True:
            send_water_reminder()
            time.sleep(interval_seconds)
            
    except KeyboardInterrupt:
        print("\nReminder stopped. Stay hydrated!")