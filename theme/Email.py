from outils import Theme
from smtplib import SMTP_SSL

class Email(Theme.Theme):
    def __init__(self):
        super().__init__("email", 2)

        super().ajouterReconnaisseur("envoi","envoie", "mail")
        super().ajouterConnecteur("a",":")

        self.gmailUser = "didierassisant@gmail.com"
        self.gmailPasswordApp = "hhodeuxdsmztiwdd"

    def action(self):
        #Recuperation des elements
        recipient = self.getElement()[0]
        utilisateurTexte = self.getElement()[1]
        emailTexte = f"Subject: Message de l'Assistant Didier.\n\n{utilisateurTexte}"

        #Connection au serveur ssl
        self.server = SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(self.gmailUser, self.gmailPasswordApp)

        #Envoi de l'email
        self.server.sendmail(self.gmailUser, recipient, emailTexte)
        self.server.close()
        resultat = f"Message envoie a {recipient}:\n{utilisateurTexte}"

        self.resetElement()
        return resultat