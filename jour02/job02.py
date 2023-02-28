class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def afficherTitre(self):
        return self.__titre

    def afficherAuteur(self):
        return self.__auteur

    def afficherPages(self):
        return self.__pages

    def changerTitre(self, titre):
        self.__titre = titre

    def changerAuteur(self, auteur):
        self.__auteur = auteur

    def changerPages(self, pages):
        if pages >= 0:
            self.__pages = pages
        else:
            print("Le nombre de pages saisies est invalide ("+str(pages)+")")

HungerGames = Livre("Hungergames /", "Suzanne Collins /", 399)
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages())

HungerGames.changerTitre("Les âmes vagabondes /")
HungerGames.changerAuteur("Stephenie Meyer /")
HungerGames.changerPages(600)
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages())

HungerGames.changerPages(0)
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages())

HungerGames.changerPages(-150)
print(HungerGames.afficherTitre(), HungerGames.afficherAuteur(), HungerGames.afficherPages())