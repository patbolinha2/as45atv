n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite mais um numero: "))
if n1 > n2 and n1 > n3:
    print("{} foi o maior numero digitado.".format(n1))
elif n2 > n1 and n2 > n3:
    print("{} foi o maior numero digitado.".format(n2))
else:
    print("{} foi o maior numero digitado.".format(n3))

if n1 < n2 and n1 < n3:
    print("{} foi o menor numero digitado.".format(n1))
elif n2 < n1 and n2 < n3:
    print("{} foi o menor numero digitado.".format(n2))
else:
    print("{} foi o menor numero digitado.".format(n3))