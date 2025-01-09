# -*- coding: utf-8 -*-
"""
thi_quiz.py

Initializes the GUI provided in thi_quiz_gui and calls it
with a list of questions provided by the data module

Created on Tue Nov 23 22:27:53 2021

@author: Lukas Lodes, Alexander Schiendorfer
"""

import thi_quiz_data as data
import thi_quiz_gui as gui

all_questions = data.load_questions_from_file("quiz_functions.txt")
# the gui expects a variable
#   all_questions -> a list 
gui.all_questions = all_questions
gui.get_next_question = data.get_random_question_from_complete_list

gui.draw_gui()
gui.main_window.mainloop()
