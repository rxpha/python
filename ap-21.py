import csv

dados = [
    {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 34, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"}
]

with open('pessoas.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor.writeheader()
    for pessoa in dados:
        escritor.writerow(pessoa)