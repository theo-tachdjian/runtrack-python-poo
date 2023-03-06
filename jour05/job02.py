def calcule(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0 :
        y = calcule(x, n/2)
        return y*y
    else:
        return x * pow(x, n-1)

entier = input("Entrez un nombre entier: ")
puissance = input("Entrez une puissance: ")
try:
    entier = int(entier)
    puissance = int(puissance)
    print(calcule(entier, puissance))
except:
    print("erreur")