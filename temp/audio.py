import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)


def getAudioListen():
    global r, mic
    #print(sr.Microphone.list_microphone_names())
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Start")
        audio = r.listen(source)
        print("Stop")
    return r.recognize_google(audio, language="fr-FR")
