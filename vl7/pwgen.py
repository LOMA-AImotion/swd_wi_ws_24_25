#adjektive = # ["Aggressiv", "Müde", "Genervt", "Lustig"]
#nomen  = #["Dinosaurier", "Politiker", "Schafe", "Autos"]

import os
adjektive_pfad = os.path.join(os.path.dirname(__file__), 'adjektive.txt')
nomen_pfad = os.path.join(os.path.dirname(__file__), 'nomen.txt')
from pw_utils import lese_von_txt_in_liste

adjektive = lese_von_txt_in_liste(adjektive_pfad)
nomen = lese_von_txt_in_liste(nomen_pfad)

if __name__ == "__main__":
    print(f"Nomen: {nomen}")
    print(f"Adjektive: {adjektive}")