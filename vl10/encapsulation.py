class StudyCourse:
    def __init__(self):
        self.__students = set()

    def add_students(self, mat_nrs : list):
        self.__students.update(mat_nrs)

    def is_immatriculated(self, mat_nr : str):
        return mat_nr in self.__students 
        

wi = StudyCourse()

# TODO which statement is better?
# wi.__students.update(["abc123@thi.de", "def456@thi.de", "hij789@thi.de"])
wi.add_students(["abc123@thi.de", "def456@thi.de", "hij789@thi.de"])
