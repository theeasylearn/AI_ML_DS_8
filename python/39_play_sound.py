# file: play_mp3_soundfile.py
import soundfile as sf #here sf is alias for soundfile
import sounddevice as sd #here sd is alias for sounddevice
data, fs = sf.read("sound/music.mp3")
sd.play(data, fs)
sd.wait()               # wait until finished (optional)
print("done.")