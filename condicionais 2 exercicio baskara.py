a, b, c = int(input()) , int(input()) , int(input())
delta =  b**2 - 4*a*c
if delta > 0:
    raiz1 = (-b + delta**(1/2)) / (2*a)
    raiz2 = (-b - delta**(1/2)) / (2*a)
    print(raiz1, raiz2)
else:
    print("Não tem raizes reais, pois delta=", delta)
