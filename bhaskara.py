a = float(input("Insira o valor de 'a': "))
b = float(input("Insira o valor de 'b': "))
c = float(input("Insira o valor de 'c': "))

delta = (b**2 - 4*a*c)
raiz1 = (-b + delta**(1/2)) / (2*a)
raiz2 = (-b - delta**(1/2)) / (2*a)

X = raiz1
Y = raiz2

if delta == 0:
   raiz1 = (-b + delta**(1/2)) / (2*a)
   print("a raiz desta equação é", X)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
if delta > 0 and X < Y:
   print("as raízes da equação são",X,"e",Y)
if delta > 0 and Y < X:
    print("as raízes da equação são",Y,"e",X)










