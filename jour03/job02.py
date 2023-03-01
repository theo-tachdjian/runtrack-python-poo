class CompteBancaire:
    def __init__(self, compte, prenom, nom, solde, decouvert=True):
        self.__compte = compte
        self.__prenom = prenom
        self.__nom = nom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Numéro de compte :", self.__compte, "\nTitulaire :", self.__prenom, self.__nom, "\nSolde :", self.__solde)

    def afficherSolde(self):
        print(self.__solde)

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
        else:
            print("Veuillez entrez un montant valide : ("+str(montant)+")")

    def agios(self):
        if self.__decouvert and self.__solde < 0:
            self.__solde = 0

    def virement(self, compte, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte.versement(montant)
        else:
            print("Le versement n'as pas pu aboutir.")

compteA = CompteBancaire("2AC5432", "Théo", "Tachdjian", 3349)
compteA.afficher()
compteA.retrait(149)
compteA.retrait(100)
compteA.versement(300)
compteA.afficherSolde()

compteB = CompteBancaire("48EK139", "Jean-Michel", "Drucker", -2148)
compteA.virement(compteB, 148)
compteA.afficher()
compteB.afficher()