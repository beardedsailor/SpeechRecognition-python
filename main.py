# convert audio file to text using sphinx(offline)
import speech_recognition as sr

# as the .wav file is in same directory 
AUDIO_FILE = "example.wav"

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio, language="en-US"))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))    
  
    
   