import string

def eh_palindromo(texto):
    texto_limpo = ''.join(
        c.lower() for c in texto if c.isalnum()
    )
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

texto = input("Digite um texto: ")
print(eh_palindromo(texto))