# Ein Modul mit nützlichen Funktionen für einen PW-Generator

def lese_von_txt_in_liste(dateipfad: str) -> list:
    """Liest aus einer Textdatei mit einem Wort pro Zeile jede Zeile in eine Liste
    Verwendet Unicode (UTF-8)

    Args:
        dateipfad (str): Pfad zur Datei die gelesen werden soll

    Returns:
        list: Liste der Wörter
    """
    with open(dateipfad, encoding="utf-8") as datei:
        zeilen = datei.read().splitlines()
    return zeilen