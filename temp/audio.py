import speech_recognition as sr
#pip install pipwin
#pipwin install pyaudio

r  = sr.Recognizer()
with sr.Microphone() as source:
    print("Dites quelque chose")
    audio = r.listen(source)