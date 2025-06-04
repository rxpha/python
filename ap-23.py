import json

# Dados da pessoa
pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo"
}

# Escrevendo os dados no arquivo JSON
with open('pessoa.json', 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

# Lendo os dados do arquivo JSON
with open('pessoa.json', 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)
    print("Dados lidos do arquivo JSON:")
    print(dados_lidos)