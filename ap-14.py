# Sistema de notas para professores

total_notas = 0
contador = 0

while True:
    nota = input("Digite a nota do aluno (0 a 10) ou 'fim' para encerrar: ")
    if nota.lower() == 'fim':
        break
    try:
        nota = float(nota)        
        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10.")            
        total_notas += nota
        contador += 1        
    except ValueError as e:
        print(f"Entrada inválida: {e}. Tente novamente.")

if contador > 0:
    media = total_notas / contador
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")