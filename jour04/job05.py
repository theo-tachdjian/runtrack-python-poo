import math
class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def aire(self):
        return self.__longueur * self.__largeur

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius

    def aire(self):
        return (self.__radius**2) * math.pi

rect = Rectangle(22, 13)
print(rect.aire())

cercle = Cercle(17)
print(cercle.aire())