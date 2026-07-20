import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")

names=['prakash','sameer','Arjun','Anjeel']

for name in names:
    speaker.speak(f"shoutout to {name}")