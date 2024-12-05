# Ziffernpad: Erstelle 9 Buttons von 1 bis 9, organisiere sie in 3x3 Gitter
import tkinter
import tkinter.messagebox
from functools import partial

def zeige_zahl(zahl:int):
    tkinter.messagebox.showinfo("THI-SWD", f"Du hast auf die Zahl {zahl} gedrückt.")

haupt_fenster = tkinter.Tk()
leinwand = tkinter.Canvas(haupt_fenster, width=400, height=400)
leinwand.grid(rowspan=3, columnspan=3)
zahler = 1

for zeile in range(0, 3):
    for spalte in range(0,3):
        neuer_button = tkinter.Button(haupt_fenster, text=zahler)
        neuer_button.config(width=10, height=5)
        neuer_button.config(command = partial(zeige_zahl, zahler))
        neuer_button.grid(column=spalte, row=zeile)
        zahler += 1
haupt_fenster.mainloop()