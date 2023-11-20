vl = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
if (
    vl < 10 or vl > 600
): 
    print("Valor inválido!")
else:
    cem = vl // 100  
    vl -= cem * 100 
    cinquenta = vl // 50 
    vl -= cinquenta * 50
    dez = vl // 10
    vl -= dez * 10
    cinco = vl // 5
    vl -= cinco * 5
    um = vl 
    if cem > 0:
        print("{} nota(s) de cem".format(cem))
    if cinquenta > 0:
        print("{} nota(s) de cinquenta".format(cinquenta))
    if dez > 0:
        print("{} nota(s) de dez".format(dez))
    if cinco > 0:
        print("{} nota(s) de cinco".format(cinco))
    if um > 0:
        print("{} nota(s) de um".format(um))