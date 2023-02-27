class Produit:
    def __init__(tomatef, nom, prixHT, TVA):
        tomatef.nom = nom
        tomatef.prixHT = prixHT
        tomatef.TVA = TVA

    def changerNom(tomatef, nom):
        tomatef.nom = nom

    def changerPrix(tomatef, prix):
        tomatef.prixHT = prix

    def changerTVA(tomatef, TVA):
        tomatef.TVA = TVA

    def Nom(tomatef):
        return tomatef.nom

    def PrixHT(tomatef):
        return tomatef.prixHT

    def tva(tomatef):
        return tomatef.TVA

    def CalculerPrixTTC(tomatef):
        return tomatef.prixHT+tomatef.TVA

    def afficher(tomatef):
        print("Nom:", tomatef.nom, "\nPrix Hors Taxes:", tomatef.prixHT, "\nTVA:", tomatef.TVA, "\nPrix TTC:", tomatef.CalculerPrixTTC())

chocolat = Produit("chocolat", 15.00, 20/100)
chocolat.afficher()

tomate = Produit("tomate", 3.65, 2.1/100)
tomate.afficher()
print(chocolat.CalculerPrixTTC())
print(tomate.CalculerPrixTTC())

chocolat.changerPrix(17.00)

tomate.changerPrix(4.50)

chocolat.afficher()
print(chocolat.Nom())
print(chocolat.PrixHT())
print(chocolat.tva())
print(chocolat.CalculerPrixTTC())

tomate.afficher()
print(tomate.CalculerPrixTTC())