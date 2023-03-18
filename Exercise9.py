# Write a program to pronounce list of names using win32 API.

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Akash", "Harry", "Digambar", "Sameesh"]
for i in l:
    speaker.Speak(f"Shoutout to {i}")
