class Joueur:
    def __init__(self, prenom, nom, position, but, passesD, Cartons_Rouge, Cartons_Jaunes):
        self.__nom = nom
        self.__prenom = prenom
        self.__position = position
        self.__but = but
        self.__passesD = passesD
        self.__Cartons_Rouge = Cartons_Rouge
        self.__Cartons_Jaunes = Cartons_Jaunes

    def marquerUnBut(self):
        self.__but += 1

    def effectuerUnePasseDecisive(self):
        self.__passesD += 1

    def recevoirUnCartonJaune(self):
        self.__Cartons_Rouge += 1

    def recevoirUnCartonRouge(self):
        self.__Cartons_Jaunes += 1

    def afficherStatistiques(self):
        print("Joueur:", self.__prenom, self.__nom,
              "\nPosition:", self.__position,
              "\nNombre de buts marqués:", self.__but,
              "\nPasses décisives:", self.__passesD,
              "\nCartons Jaunes:", self.__Cartons_Rouge,
              "\nCartons Rouges:", self.__Cartons_Jaunes)

class Equipe:
    def __init__(self, nom, liste_joueurs: list[Joueur]):
        self.__nom = nom
        self.__liste_joueurs = liste_joueurs

    def ajouterJoueur(self, joueur):
        self.__liste_joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        print("Joueurs de l'équipe " + self.__nom + ":")
        for joueur in self.__liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, but=False, passe_decisive=False, carton_jaune=False, carton_rouge=False):
        try:
            joueur_in = self.__liste_joueurs[self.__liste_joueurs.index(joueur)]
            if but:
                joueur_in.marquerUnBut()
            if passe_decisive:
                joueur_in.effectuerUnePasseDecisive()
            if carton_jaune:
                joueur_in.recevoirUnCartonJaune()
            if carton_rouge:
                joueur_in.recevoirUnCartonRouge()
        except:
            print("Le Joueur n'existe pas")

Franz = Joueur("Franz", "Beckenbauer", "Défenseur", 0, 6, 1, 0)
David = Joueur("David", "Beckham", "Attaquant", 6, 7, 2, 0)
George = Joueur("George", "Best", "Attaquant", 8, 3, 1, 1)

Éric = Joueur("Éric", "Cantona", "Défenseur", 0, 6, 1, 0)
Bobby = Joueur("Bobby", "Charlton", "Attaquant", 6, 7, 2, 0)
Johan = Joueur("Johan", "Cruyff", "Attaquant", 8, 3, 1, 1)

equipe1 = Equipe("équipe 1", [Franz, David, George])
equipe2 = Equipe("équipe 2", [Éric, Bobby, Johan])
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(David, but=True, carton_jaune=True)
equipe2.mettreAJourStatistiquesJoueur(Bobby, passe_decisive=True, carton_rouge=True)
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()