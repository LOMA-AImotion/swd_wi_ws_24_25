class Quiz:
    def __init__(self, name, diff, questions):
        self.name = name
        self.diff = diff
        self.questions = questions
    
    def start(self):
        pass
    
class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    
class Answer: 
    def __init__(self, text, correct):
        self.text = text
        self.correct = correct
        

q1 = Question("What is 2+2", [Answer("4", True), Answer("1", False)])
q2 = Question("What is 2+5", [Answer("4", False), Answer("5", False), Answer("Four", True)])
quiz = Quiz("Math", "easy", [q1, q2])


 