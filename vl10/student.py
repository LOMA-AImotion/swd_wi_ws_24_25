class Student:
    def __init__(self, vorname: str, nachname: str, mat_nr: int):
        self.vorname = vorname
        self.nachname = nachname
        self.mat_nr = mat_nr

    def pruefung(self):
        print(f"Mein Name ist {self.vorname} {self.nachname}, meine MatNr ist {self.mat_nr}")

if __name__ == "__main__":
    s = Student("Hans", "Wurst", 1234)
    s.nachname = "Salami"
    s.pruefung()
    print(type(s))
