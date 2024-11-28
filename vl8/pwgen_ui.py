import tkinter
from pwgen import generiere_passwort

def neues_passwort_anzeigen():
    neues_passwort = generiere_passwort()
    print(neues_passwort)
    password_label.config(text=f"Generiertes Passwort: {neues_passwort}")

haupt_fenster = tkinter.Tk()
canvas = tkinter.Canvas(haupt_fenster, width=200, height=300)
canvas.grid(rowspan=2, columnspan=1) 
password_gen_button = tkinter.Button(haupt_fenster, text="Generiere Passwort", 
                                     command=neues_passwort_anzeigen)
password_gen_button.grid(row=0, column=0)

password_label = tkinter.Label(haupt_fenster, text="Generiertes Passwort: ")
password_label.grid(row=1, column=0)
haupt_fenster.mainloop()