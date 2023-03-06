def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n-1)

user_input = input("Donner un nombre superieur ou égal à 0 : ")
try:
    print(facto(int(user_input)))
except:
    print("erreur")