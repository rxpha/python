# Sistema de Números Inteiros Pares ou Ímpares

while True:
    numero = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if numero.lower() == 'fim':
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"{numero} é um número par.")
        else:
            print(f"{numero} é um número ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

