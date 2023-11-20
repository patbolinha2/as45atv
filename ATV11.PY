salario_anterior = float(input("Digite seu salário atual: "))
salario_atual = 0.0
diferenca_entre_salarios = 0.0
percentual_de_aumento = 0.0

if salario_anterior <= 280:
    percentual_de_aumento = 20
elif salario_anterior <= 750:
    percentual_de_aumento = 15
elif salario_anterior <= 1500:
    percentual_de_aumento = 10
else:
    percentual_de_aumento = 5

diferenca_entre_salarios = salario_anterior * (percentual_de_aumento / 100)
salario_atual = salario_anterior + diferenca_entre_salarios
print("Seu salário antes do reajuste era de R${}".format(salario_anterior))
print("Seu salário foi aumentado em {}%".format(percentual_de_aumento))
print("Seu salário foi aumentado em R${}".format(diferenca_entre_salarios))
print("Seu salário atual é de R${}".format(salario_atual))