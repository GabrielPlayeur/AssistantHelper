import speech_recognition as sr
from tkinter import messagebox

class GestionAudio:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.aMicro = True
        try:
            self.micro = sr.Microphone()
        except OSError: #Pas de micro trouvé sur le PC
            self.micro = None
            self.aMicro = False
        
    def ecouter(self):
        """
            Entree:
            Sortie: str
            Fonction: ecoute l'entree de son donne pour ensuite convertir le son recu en texte
        """
        if not self.aMicro:
            return "Pas de micro connecté au PC"
        texteCompris = ""
        with self.micro as source:
            self.recognizer.adjust_for_ambient_noise(source)            
            messagebox.showinfo(title="Ecoute micro", message="L'assistant est près à vous écouter appuier sur ok pour commencer à parler")
            try:
                audio = self.recognizer.listen(source, timeout=10)
                texteCompris = self.recognizer.recognize_google(audio, language="fr-FR")
            except sr.WaitTimeoutError:
                texteCompris = "Rien n'a ete entendu"
        return texteCompris