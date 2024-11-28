def volumen(breite: int, hoehe: int, tiefe: int, 
            preis_pro_m3:int = 5, steuer_satz:float = 1.19):
    return breite * hoehe * tiefe * preis_pro_m3 * steuer_satz

print(volumen(10, 5, 20))