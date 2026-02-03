import pyttsx3

engine = pyttsx3.init()

# Optional tweaks
engine.setProperty('rate', 150)    # words per minute
engine.setProperty('volume', 0.9)  # 0.0–1.0

# List available voices
voices = engine.getProperty('voices')
# for voice in voices: print(voice.name, voice.id)

# engine.setProperty('voice', voices[1].id)  # change if wanted

engine.say("Hello! This is completely offline with no API key needed. Works on Windows, macOS and Linux.")
engine.runAndWait()

# Save to file instead of speaking
engine.save_to_file("Text to WAV example.", "hello_offline.wav")
engine.runAndWait()