class Livre:
    def __init__(self, titre, auteur, pages, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = disponible

    def afficherTitre(self):
        return self.__titre

    def afficherAuteur(self):
        return self.__auteur

    def afficherPages(self):
        return self.__pages

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.vérification():
            self.__disponible = False

    def rendre(self):
        if not self.vérification():
            self.__disponible = True

HungerGames = Livre("Hunger Games /", "Suzanne Collins /", 399)
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages(), HungerGames.vérification())

HungerGames.rendre()
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages(), HungerGames.vérification())

HungerGames.emprunter()
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages(), HungerGames.vérification())

HungerGames.emprunter()
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages(), HungerGames.vérification())

HungerGames.rendre()
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages(), HungerGames.vérification())