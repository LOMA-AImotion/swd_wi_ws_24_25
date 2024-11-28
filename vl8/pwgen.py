#adjektive = # ["Aggressiv", "Müde", "Genervt", "Lustig"]
#nomen  = #["Dinosaurier", "Politiker", "Schafe", "Autos"]

import os
import random
adjektive_pfad = os.path.join(os.path.dirname(__file__), 'adjektive.txt')
nomen_pfad = os.path.join(os.path.dirname(__file__), 'nomen.txt')
from pw_utils import lese_von_txt_in_liste

def generiere_passwort(nomen_pfad = nomen_pfad, adjektive_pfad = adjektive_pfad, 
                       obere_grenze : int = 100):    
    adjektive = lese_von_txt_in_liste(adjektive_pfad)
    nomen = lese_von_txt_in_liste(nomen_pfad)
    adjektiv = random.choice(adjektive)
    gewaehltes_nomen = random.choice(nomen)
    zahl = random.randint(0, obere_grenze)
    sonderzeichen = random.choice("§*/&%+?#")
    passwort = adjektiv + gewaehltes_nomen + str(zahl) + sonderzeichen
    return passwort

if __name__ == "__main__":
    print(generiere_passwort())