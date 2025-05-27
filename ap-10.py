# Cálculo de IMC

peso = float(input("Digite o seu peso (em kg): "))
altura = int(input("Digite a sua altura (em centimetros): "))

altura = altura / 100  # Convertendo altura para metros
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, você está abaixo do peso.')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f}, você está com o peso normal.')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f}, você está com sobrepeso.')
else:
    print(f'Seu IMC é {imc:.2f}, você está obeso.')