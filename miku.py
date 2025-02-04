import time
import random
from gtts import gTTS
import os

def fake_wifi_scan():
    """Pretends to scan the router for hidden data."""
    print("[*] Scanning router for hidden data...")
    time.sleep(2)

    fake_devices = [
        "192.168.1.2 - Smart Fridge",
        "192.168.1.3 - Unknown Device",
        "192.168.1.4 - Security Camera",
        "192.168.1.5 - Miku (???)"
    ]

    for device in fake_devices:
        print(f"[*] Found device: {device}")
        time.sleep(random.uniform(0.5, 1.5))

    print("\n[*] WARNING: Unusual activity detected...")
    time.sleep(2)
    print("[*] Trying to access hidden files in the router...\n")
    time.sleep(2)

    # Miku appears!
    print("✨ Miku has been found inside your router! ✨")
    time.sleep(1)

    return True

def say_hatsune_miku():
    """Say Hatsune Miku using gTTS."""
    text = "Hatsune Miku"
    tts = gTTS(text=text, lang='en')
    tts.save("hatsune_miku.mp3")
    os.system("mpv --quiet hatsune_miku.mp3 > /dev/null 2>&1")  # Play the MP3 file quietly

def play_youtube_audio():
    """Play the audio from a YouTube video using yt-dlp and mpv."""
    print("\n🎶 Miku is singing! 🎶\n")
    url = "https://youtu.be/RAPWUXxvYpE?si=0h4wi-QLwSIdr0_2"  # Replace with your desired YouTube URL
    os.system(f"yt-dlp -q -o - {url} | mpv --quiet - > /dev/null 2>&1")  # Stream and play the audio quietly

# Run the fake scan, say Hatsune Miku, and play the YouTube audio
if fake_wifi_scan():
    say_hatsune_miku()  # Say "Hatsune Miku"
    play_youtube_audio()  # Play the audio from the YouTube video
