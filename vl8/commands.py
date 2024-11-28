import tkinter
import tkinter.messagebox

def sag_hallo():
    tkinter.messagebox.showinfo("THI-SWD", "Servus")
    print("Servus")

haupt_fenster = tkinter.Tk()
button = tkinter.Button(haupt_fenster, text="Sag Hallo", command=sag_hallo)
button.pack()
haupt_fenster.mainloop()