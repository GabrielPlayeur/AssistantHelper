import sys
import subprocess
import platform

#---------------------------Installation de PyAudio-----------------------------------------
versionPythonListe = platform.python_version_tuple() #recupere la verison de python utilise
versionPython = f"{versionPythonListe[0]}{versionPythonListe[1]}"
if len(versionPython) > 3:
    versionPython += f"{versionPythonListe[2]}"
ajoutLettre = ""
if versionPythonListe[1] == '7': #Je ne sais pas pourquoi le fiche python 3.7 a besoin de ce m en plus mais en le supprimant du nom l'installation ne fonctionne plus
    ajoutLettre = "m"
pyAudioPath = sys.path[0]+f"\\libs\\PyAudio-0.2.11-cp{versionPython}-cp{versionPython}{ajoutLettre}-win_amd64.whl" #Mise en forme du chemain vers le ficher wheel a installer
subprocess.check_call([sys.executable, '-m', 'pip', 'install','--upgrade',pyAudioPath]) #Installation avec une commande pip
#-------------------------------------------------------------------------------------------


listeModule = ["SpeechRecognition","unidecode","bs4","tzwhere","geopy","tweepy","autocorrect"] #Liste des autres modules utilise par l'assistant

for module in listeModule:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','--upgrade',module]) #Installation de chaque module avec la commande pip