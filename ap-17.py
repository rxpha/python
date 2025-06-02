def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:    
    return valor_conta * (porcentagem_gorjeta / 100)

valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"A gorjeta é: R$ {gorjeta:.2f}")