class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def entrer_nb_habitants(self):
        return self.__nb_habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville._Ville__nb_habitants += 1

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print("Population de la ville de Paris: ", paris.entrer_nb_habitants(), "habitants")
print("Population de la ville de Paris: ", marseille.entrer_nb_habitants(), "habitants")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print("Mise à jour de la population de la ville de Paris: ", paris.entrer_nb_habitants(), "habitants")
print("Mise à jour de la population de la ville de Paris: ", marseille.entrer_nb_habitants(), "habitants")