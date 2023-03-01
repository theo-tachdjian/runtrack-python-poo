effet = ["À faire", "Terminée"]
class Tache:
    def __init__(self, entete, desc, statut: bool):
        self.__entete = entete
        self.__desc = desc
        self.__statut = statut

    def ajout_entete(self):
        return self.__entete

    def ajout_desc(self):
        return self.__desc

    def ajout_statut(self):
        return self.__statut

    def rplce_statut(self, statut: bool):
        self.__statut = statut

class ListeDeTaches:
    def __init__(self, taches: list[Tache] = []):
        self.__taches = taches

    def ajouterTache(self, tache: Tache):
        self.__taches.append(tache)

    def supprimerTache(self, tache):
        try:
            self.__taches.remove(tache)
        except:
            print("aucune tache de ce nom n'est enregistrer.")

    def marquerCommeFinie(self, tache):
        try:
            self.__taches[self.__taches.index(tache)].rplce_statut(True)
        except:
            print("aucune tache de ce nom n'est enregistrer.")

    def afficherListe(self):
        for tache in self.__taches:
            print(tache.ajout_entete(), tache.ajout_desc(), effet[tache.ajout_statut()])

    def filtrerListe(self, statut: bool):
        print("Affichage des taches avec le statut:", effet[statut])
        for tache in self.__taches:
            if tache.ajout_statut() == statut:
                print(tache.ajout_entete(), tache.ajout_desc())

tache1 = Tache("Adopter un animal", "faire en sorte qu'il survive", False)
tache2 = Tache("Adopter un enfant", "faire en sorte qu'il survive", False)
tache3 = Tache("Vendre l'animal", "ça coute trop chere à faire survivre", False)
tache4 = Tache("Vendre l'enfant en morceau", "ça rapporte plus que de le faire survivre", False) # c'est une vanne au cas où

liste = ListeDeTaches([tache1, tache2, tache3])
liste.afficherListe()

liste.marquerCommeFinie(tache3)
liste.filtrerListe(True)

liste.ajouterTache(tache4)
liste.afficherListe()

liste.supprimerTache(tache4)
liste.afficherListe()