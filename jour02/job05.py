class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def enter_marque(self):
        return self.__marque

    def ajout_marque(self, marque):
        self.__marque = marque

    def enter_modele(self):
        return self.__modele

    def ajout_modele(self, modele):
        self.__modele = modele

    def enter_annee(self):
        return self.__annee

    def ajout_annee(self, annee):
        self.__annee = annee

    def enter_kilometrage(self):
        return self.__kilometrage

    def ajout_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def enter_en_marche(self):
        return self.__en_marche

    def ajout_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir

voiture = Voiture("Peugeot", "107", 2012, 165000)
voiture.demarrer()
print(voiture.enter_en_marche())

voiture.arreter()
print(voiture.enter_en_marche())

voiture2 = Voiture("Peugeot", "107", 2012, 165000, reservoir=5)
voiture2.demarrer()
print(voiture.enter_en_marche())