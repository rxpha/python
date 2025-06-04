import csv

arquivo_csv = 'pessoas.csv'  # Altere para o caminho do seu arquivo CSV

with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
    leitor = csv.DictReader(csvfile)
    print(f"{'Nome':<20} {'Idade':<5} {'Cidade':<20}")
    print('-' * 45)
    for linha in leitor:
        print(f"{linha['Nome']:<20} {linha['Idade']:<5} {linha['Cidade']:<20}")