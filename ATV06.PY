n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite mais um numero: "))
if n1 > n2 and n1 > n3:
    print("{n1} foi o maior numero digitado.")
elif n2 > n1 and n2 > n3:
    print("{n2} foi o maior numero digitado.")
else:
    print("{n3} foi o maior numero digitado.")