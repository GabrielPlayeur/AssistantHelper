import speech_recognition as sr

class GestionAudio:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.micro = sr.Microphone()
        
    def ecouter(self):
        """
            Entree:
            Sortie: str
            Fonction: ecoute l'entree de son donne pour ensuite convertir le son recu en texte
        """
        texteCompris = ""
        with self.micro as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.affichage("Start")
            try:
                audio = self.recognizer.listen(source, timeout=15)
                texteCompris = self.recognizer.recognize_google(audio, language="fr-FR")
            except sr.WaitTimeoutError:
                texteCompris = "Rien n'a ete entendu"            
            self.affichage("End")
        return texteCompris            
            
    def affichage(self, texte: str):
        """
            Entree: texte (str)
            Sortie:
            Fonction: Afficher le texte donne en parametre
        """
        print(texte)