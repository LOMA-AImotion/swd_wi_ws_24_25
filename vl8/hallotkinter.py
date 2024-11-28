import tkinter
haupt_fenster = tkinter.Tk()
leinwand = tkinter.Canvas(haupt_fenster, width=200, height=400)
leinwand.grid(row=0, column=0, columnspan=2, rowspan=4)

label = tkinter.Label(haupt_fenster, text="Servus WI")
label.grid(column=0, row=0)
button = tkinter.Button(haupt_fenster, text="OK")
button.grid(column=0, row=3, columnspan=2)

test_button = tkinter.Button(haupt_fenster, text="Außerhalb")
test_button.grid(row=5, column=4)
haupt_fenster.mainloop()