li = float(input("Digite quantos litros você quer abastecer: "))
comb = input("Digite A para álcool ou G para gasolina: ")
pre = 0
if comb == "A" or comb == "a":
    pre = li * 1.9
    if li <= 20:
        pre -= 1.9 * li * 3 / 100
    else:
        pre -= 1.9 * li * 5 / 100
elif comb == "G" or comb == "g":
    pre= li * 2.5
    if li <= 20:
        pre -= 2.5 * li * 4 / 100
    else:
        pre -= 2.5 * li * 6 / 100
print("O preço a pagar é R${}".format(pre))