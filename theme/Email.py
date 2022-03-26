from outils import Theme
from smtplib import SMTP_SSL

class Email(Theme.Theme):
    def __init__(self):
        super().__init__("email", 2)

        super().ajouterReconnaisseur("envoi","envoie","envoyer","lettre","annonce","courrier","destinataire")
        super().ajouterConnecteur("a",":")

        self.gmailUser = "didierassisant@gmail.com"
        self.gmailPasswordApp = "hhodeuxdsmztiwdd"

    def action(self):
        recipient = self.getElement()[0]
        emailTexte = self.getElement()[1]

        self.server = SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(self.gmailUser, self.gmailPasswordApp)

        self.server.sendmail(self.gmailUser, recipient, emailTexte)
        self.server.close()
        resultat = f"Message envoie a {recipient}: {emailTexte}"

        self.resetElement()
        return resultat