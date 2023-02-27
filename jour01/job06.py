class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

variable = Animal()
print("L'age de l'animal", variable.age, "ans")
variable.vieillir()
print("L'age de l'animal", variable.age, "ans")
variable.nommer("Pilou")
print("L'animal se nomme", variable.prenom)