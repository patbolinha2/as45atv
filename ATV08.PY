p1 = float(input("Digite o preço do produto 1: "))
p2 = float(input("Digite o preço do produto 2: "))
p3 = float(input("Digite o preço do produto 3: "))
if p1 < p2 and p1 < p3:
    print("O produto com o menor preco é o 1, custando R${}".format(p1))
elif p2 < p1 and p2 < p3:
    print("O produto com o menor preco é o 2, custando R${}".format(p2))
else:
    print("O produto com o menor preco é o 3, custando R${}".format(p3))