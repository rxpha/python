# Classificador de Idade

idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("De acordo com a idade descrita você é uma criança.")
elif idade < 18:
    print("De acordo com a idade descrita você é um adolescente.")
elif idade < 60:
    print("De acordo com a idade descrita você é um adulto.")
else:
    print("De acordo com a idade descrita você é um idoso.")
