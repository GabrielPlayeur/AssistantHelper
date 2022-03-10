import speech_recognition as sr

class GestionAudio:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.micro = sr.Microphone()
        
    def ecouter(self):
        texteCompris = ""
        with self.micro as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.affichage("Start")
            try:
                audio = self.recognizer.listen(source, timeout=15)
                texteCompris = self.recognizer.recognize_google(audio, language="fr-FR")
            except sr.WaitTimeoutError:
                self.affichage("Rien n'a ete entendu")
        return texteCompris
            
            
    def affichage(self, texte):
        print(texte)