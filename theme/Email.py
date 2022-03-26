from outils import Theme
from smtplib import SMTP_SSL

class Email(Theme.Theme):
    def __init__(self):
        super().__init__("email", 2)

<<<<<<< HEAD
        super().ajouterReconnaisseur("envoi","envoie", "mail")
=======
        super().ajouterReconnaisseur("envoi","envoie","envoyer","lettre","annonce","courrier","destinataire")
>>>>>>> 0afc1e90c019a0eacffef177af048d6a56d83500
        super().ajouterConnecteur("a",":")

        self.gmailUser = "didierassisant@gmail.com"
        self.gmailPasswordApp = "hhodeuxdsmztiwdd"

    def action(self):
        #Recuperation des elements
        recipient = self.getElement()[0]
<<<<<<< HEAD
        utilisateurTexte = self.getElement()[1]
        emailTexte = f"Subject: Message de l'Assistant Didier.\n\n{utilisateurTexte}"

        #Connection au serveur ssl
=======
        emailTexte = self.getElement()[1]

>>>>>>> 0afc1e90c019a0eacffef177af048d6a56d83500
        self.server = SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(self.gmailUser, self.gmailPasswordApp)

        #Envoi de l'email
        self.server.sendmail(self.gmailUser, recipient, emailTexte)
        self.server.close()
        resultat = f"Message envoie a {recipient}:\n{utilisateurTexte}"

        self.resetElement()
        return resultat