import win32com.client
import datetime

# Create speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Get current hour
hour = datetime.datetime.now().hour

# Your name
name = "Prakash"

# Greeting based on time
if 5 <= hour < 12:
    greeting = f"Good Morning, {name}! Have a wonderful day."
elif 12 <= hour < 17:
    greeting = f"Good Afternoon, {name}! Hope your day is going well."
elif 17 <= hour < 21:
    greeting = f"Good Evening, {name}! Welcome back."
else:
    greeting = f"Hello, {name}! It's getting late. Take care."

print(greeting)
speaker.Speak(greeting)