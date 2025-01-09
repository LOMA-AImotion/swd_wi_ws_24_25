# -*- coding: utf-8 -*-
"""
thi_quiz_gui.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""

import tkinter as tk
# Sometimes the explicit import is necessary
from tkinter import messagebox
#from tkinter import ttk
from functools import partial

# Its not necessary to declare the global variables twice, but it adds
# some more explicity and improves visibility of these variables
correct_index = None
all_questions = None
get_next_question = None

path_to_image = "quiz_logo.png" 
# path_to_image = "quiz_logo.png"
# Depending on your IDE, you may need to pass an explicit path
# path_to_image = "C:\path\to\image\quiz_logo.png"
options = "ABCD"
# options = "1234"
def answered(i):
    """
    Compares the given answer with the solution. 

    Args:
        i: integer, the index (starting at 0) of the given answer.
    """
    global correct_index
    print(f"I got the answer {i}")
    if i == correct_index:
        tk.messagebox.showinfo("Well done", "That is indeed correct, congrats.")
        draw_gui() # Reload GUI with new question
    else:
        tk.messagebox.showerror("Try again", "That was not correct, try again.")


def draw_gui():
    """
    Retrieves the next question and updates the texts in the GUI.    
    """

    global correct_index

    # Here we actually call the stored function reference
    question = get_next_question(all_questions)
    question_text, a1, a2, a3, a4, correct_idx = question
    answers = [a1, a2, a3, a4]
    
    correct_index = correct_idx # We can only access, but not modify global variables!
    
    quest_var.set(question_text)
    for k, val in enumerate(answers): 
        # convert i to row and col index
        answer_vars[k].set(options[k] + ") " +val)


main_window:tk.Tk = tk.Tk()
main_window.title("THI Quiz")

canvas = tk.Canvas(main_window, width=600, height = 300)
canvas.grid(columnspan=2, rowspan=4)

logo_tk = tk.PhotoImage(file=path_to_image)
logo_label = tk.Label(main_window, image = logo_tk)

logo_label.grid(row = 0, column = 0, columnspan = 2)

# question label 
quest_var = tk.StringVar()
quest_var.set("Hi there")

quest_label = tk.Label(main_window, textvariable=quest_var, font = ("Arial 18 bold"))

quest_label.grid(row = 1, column = 0, columnspan = 2)

answer_vars = [ tk.StringVar(main_window, f"Answer {i}") for i in range(0, 4)]

# Another possibility would be 4 explicit statements for each button
for i in range(0, 2):
    for j in range(0, 2):
        answer_button = tk.Button(main_window, 
                                textvariable = answer_vars[i * 2 + j], 
                                font = ("Arial 14"),
                                # Allows the answered function to be called with the correct index.
                                # Another solution would involve hardcoding answered functions for
                                # all 4 buttons with
                                command = partial(answered, i*2 + j)
                                )
        
        answer_button.grid(row = 2+i, column = j)
