from tkinter import messagebox

class Feedbacker:
    def positive(self):
        pass

    def negative(self):
        pass    

class PrintFeedbacker(Feedbacker):
    def positive(self):
        print("Great!")

    def negative(self):
        print("Oh no!")

class TkinterFeedbacker(Feedbacker):
    def positive(self):
        messagebox.showinfo("Feedback", "Great!")

    def negative(self):
        messagebox.showerror("Feedback", "Try again!")

if __name__ == "__main__":
    if input("Print or Tkinter? ") == "Print":
        feedbacker = PrintFeedbacker()
    else:
        feedbacker = TkinterFeedbacker()

    feedbacker.positive()
    feedbacker.negative()