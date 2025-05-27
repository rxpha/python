# Mini Calculadora

def calcular(operador, num1, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Erro: Não é possível dividir por zero"
    else:
        return "Operador inválido!"
    

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador not in ['+', '-', '*', '/']:
        raise ValueError("Operador inválido!")
except ValueError:
    print("Por favor, digite um número válido.")
resultado = calcular(operador, num1, num2)

print(f"O resultado de {num1} {operador} {num2} é: {resultado}")