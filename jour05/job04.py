def comptage(chaine):
    if len(chaine) == 1:
        return chaine[0]
    else:
        x = chaine[0]
        y = chaine[1:]
        z = comptage(y)
        if x > z:
            return x
        else:
            return z

chaine = input("Écrivez vos chiffre sans mettre d'espace : ")
chaine = [int(chiffre) for chiffre in chaine]
try :
    sortie = comptage(chaine)
    print(f"{chaine} à pour plus grand chiffre {sortie}")
except:
    print("erreur")