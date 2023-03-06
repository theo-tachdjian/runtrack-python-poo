def Fibonacci(n):
    return suite_Fibonacci(n, 0, 1)

def suite_Fibonacci(n, a, b):
    if n == 3:
        return a+b
    elif n == 2:
        return b
    elif n == 1:
        return a
    elif n == 0:
        return None
    else:
        return suite_Fibonacci(n-1, b, a+b)

user_input = input("Donner un nombre (n-ième nombre de la suite de Fibonacci): ")
try:
    print(Fibonacci(int(user_input)))
except Exception as e:
    print("Entrée invalide:", str(e))