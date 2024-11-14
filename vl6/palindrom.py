# Prüfe ob eine Zeichenkette ein Palindrom ist oder nicht.
# 

def ist_palindrom(zeichenkette: str) -> bool:
    """ überprüft ob eine Zeichenkette von vorne und hinten gelesen gleich ist. 
    Nimmt dabei Rücksicht auf Groß/Kleinschreibung

    Args:
        zeichenkette (str): 

    Returns:
        bool: 
    """
    rev_zeichenkette = zeichenkette[::-1]
    return rev_zeichenkette == zeichenkette

if __name__ == "__main__":
    zeichenkette = input("Zeichenkette?")

    print(ist_palindrom(zeichenkette))