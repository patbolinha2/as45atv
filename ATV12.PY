valor_da_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = valor_da_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = salario_bruto * (desconto_ir / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11 / 100)
total_de_descontos = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(
    "\nSalário Bruto     : R${}",
    "\n(-) IR (5%)       : R${}",
    "\n(-) INSS ( 10%)   : R${}",
    "\nFGTS (11%)        : R${}",
    "\nTotal de descontos: R${}",
    "\nSalário Liquido   : R${}"
    .format(salario_bruto,IR,INSS,FGTS,total_de_descontos,salario_liquido),
)

