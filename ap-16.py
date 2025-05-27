# Verificador de Segurança de Senhas

while True:
    senha = input("Digite uma senha ou 'sair': ")

    if senha.lower() == 'sair': 
        break

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
    elif not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
    else:        
        print("Senha válida.")
        break