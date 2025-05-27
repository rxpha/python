# Conversor de Temperatura

temperatura = float(input("Digite a temperatura atual: "))
unidade_atual = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
unidade_convertida = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
temperatura_convertida = 0.0

if unidade_atual == 'C':
    if unidade_convertida == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_convertida == 'K':
        temperatura_convertida = temperatura + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_atual == 'F':
    if unidade_convertida == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_convertida == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_atual == 'K':
    if unidade_convertida == 'C':
        temperatura_convertida = temperatura - 273.15
    elif unidade_convertida == 'F':
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperatura_convertida = temperatura

print(f'A temperatura atual é: {temperatura:.2f} {unidade_atual}')
print(f'A temperatura convertida é: {temperatura_convertida:.2f} {unidade_convertida}')