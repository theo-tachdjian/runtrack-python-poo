class Rectangle :
    def __init__(self, longueur, largeur) :
        self.__longueur = longueur
        self.__largeur = largeur

    def périmètre(self) :
        return (self.__longueur + self.__largeur)*2

    def surface(self) :
        return self.__longueur*self.__largeur

    def entrer_Longueur(self) :
        return self.__longueur

    def rplacer_Longueur(self, longueur) :
        self.__longueur = longueur

    def entrer_Largeur(self) :
        return self.__largeur

    def rplacer_Largeur(self, largeur) :
        self.__largeur = largeur

class Parallélépipède(Rectangle) :
    def __init__(self, longueur, largeur, hauteur) :
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self) :
        return self.entrer_Longueur()*self.entrer_Largeur()*self.__hauteur

rect = Rectangle(22, 13)
print("Longueur =", rect.entrer_Longueur()," / ", "Largeur =", rect.entrer_Largeur()," / ", "Périmètre =", rect.périmètre()," / ", "Surface =", rect.surface())
rect.rplacer_Longueur(20)
rect.rplacer_Largeur(10)
print("Longueur =", rect.entrer_Longueur()," / ", "Largeur =", rect.entrer_Largeur()," / ", "Périmètre =", rect.périmètre()," / ", "Surface =", rect.surface())

paral = Parallélépipède(15, 15, 6)
print("\nVolume =", paral.volume())
