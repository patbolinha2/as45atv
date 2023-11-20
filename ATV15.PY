n1 = float(input("Digite o primeiro lado do triângulo: "))
n2 = float(input("Digite o segundo lado do triângulo: "))
n3 = float(input("Digite o terceiro lado do triângulo: "))

if (
    (n1 + n2 > n3)
    and (n1 + n3 > n2)
    and (lado2 + lado3 > lado1)
):
    if (n1 == n2) and (n2 == n3):
        print("É um triângulo equilátero!")
    elif (n1 == n2) or (n1 == n3) or (n2 == n3):
        print("É um triângulo isósceles!")
    else:
        print("É um triângulo escaleno!")
else:
    print("Não é um triângulo!")