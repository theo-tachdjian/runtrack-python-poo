class Personne:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)

personnes = [
    Personne("John", "Doe"),
    Personne("Jean", "Dupont"), ]

for personne in personnes:
    personne.SePresenter()