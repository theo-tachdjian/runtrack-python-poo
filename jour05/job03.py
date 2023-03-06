def taille(caracteres):
    if caracteres =="":
        return 0
    else:
        caracteres[0]
        return 1 + taille(caracteres[1:])

utilisateur = input("Entrez votre phrase : ")
print(taille(utilisateur))