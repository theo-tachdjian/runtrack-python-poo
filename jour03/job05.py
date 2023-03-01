import random
class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def creat_Nom(self):
        return self.__nom

    def creat_Vie(self):
        return self.__vie

    def enlever_Vie(self, nbre):
        self.__vie -= nbre
        print(self.__nom, "subit", nbre,"dégats !")

    def attaquer(self, personnage):
        print(self.__nom, "attaque", personnage.creat_Nom(), "!")
        personnage.enlever_Vie(random.randint(1, 6))

    def soigner(self):
        nbre = random.randint(2, 6)
        if nbre > 2:
            self.__vie += nbre
            print("\nSoin de", nbre, "PV pour", self.__nom, "!")
        else:
            print("\nLe pouvoir SOINS de", self.__nom, "a raté !")

class Jeu:
    def __init__(self):
        self.__niveau = 0

    def level(self):
        user_input = input("difficulté -1 Easy, -2 Normal, -3 Hard :\n")
        try:
            user_input = int(user_input)
            if 1 <= user_input <= 3:
                self.__niveau = user_input
                self.lancerJeu(self.__niveau)
            else:
                print("L'action n'as pas été comprise")
        except:
            print("L'action n'as pas été comprise")

    def lancerJeu(self, niveau):
        running = True
        Héros: Personnage
        ennemi: Personnage
        if niveau == 2:
            Héros = Personnage("Héros", 25)
            ennemi = Personnage("Blobby le blob", 25)
        elif niveau == 3:
            Héros = Personnage("Héros", 20)
            ennemi = Personnage("Blobby le blob", 30)
        else:
            Héros = Personnage("Héros", 20)
            ennemi = Personnage("Blobby le blob", 15)
        while running:
            self.afficher_stats(Héros, ennemi)
            input_valide = False
            while not input_valide:
                print("-\t1: ATTAQUER\n-\t2: SOINS")
                user_input = input("Quelle action choisissez-vous ?\n")
                try:
                    user_input = int(user_input)
                    if 1 <= user_input <= 2:
                        input_valide = True
                        print()
                        self.action(Héros, ennemi, user_input)
                    else:
                        print("L'entrée n'est pas valide !")
                except:
                    print("L'entrée n'est pas valide !")
            if ennemi.creat_Vie() > 0:
                self.action(ennemi, Héros, random.randint(1, 2))
            running = self.vérif_stats(Héros, ennemi)

    def action(self, personnage, adversaire, index):
        if index == 2:
            personnage.soigner()
        else:
            personnage.attaquer(adversaire)

    def afficher_stats(self, Héros, ennemi):
        print()
        print(Héros.creat_Nom(), ":", Héros.creat_Vie())
        print(ennemi.creat_Nom(), ":", ennemi.creat_Vie())

    def vérif_stats(self, Héros, ennemi):
        if ennemi.creat_Vie() <= 0:
            print("\nFélicitation vous avez vaincu")
            return False
        elif Héros.creat_Vie() <= 0:
            print("\nOh non, vous avez péris...")
            return False
        return True

jeu = Jeu()
jeu.level()