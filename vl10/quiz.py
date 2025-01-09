class Frage:
    def __init__(self, frage: str, alternativen: list, korrekter_index: int):
        self.frage = frage
        self.alternativen = alternativen
        self.korrekter_index = korrekter_index
 
    def antwort_korrekt(self, antwort: str) -> bool:
        return antwort == self.alternativen[self.korrekter_index]
    
    def index_korrekt(self, antwort_index: int) -> bool:
        return antwort_index == self.korrekter_index
    
if __name__ == "__main__":
    f = Frage("Was ist 2+2?", ["Frag ChatGPT", "4", "5", "egal"], 1)
    print(f.antwort_korrekt("4"))
    print(f.antwort_korrekt("5"))
    print(f.index_korrekt(0))
    print(f.index_korrekt(1))