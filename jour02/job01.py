class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def afficherLongueur(self):
        print("Le rectangle a une longueur de : ", self.__longueur)
    def afficherLargeur(self):
        print("et un largeur de : ", self.__largeur)

    def changerLongueur(self, longueur):
        self.__longueur = longueur

    def changerLargeur(self, largeur):
        self.__largeur = largeur

rect = Rectangle(32, 25)
print(rect.afficherLongueur(), rect.afficherLargeur())

rect.changerLongueur(18)
rect.changerLargeur(12)
print(rect.afficherLongueur(), rect.afficherLargeur())