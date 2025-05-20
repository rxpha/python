nome_produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o preço unitário do produto: '))
quantidade_produto = int(input('Digite a quantidade do produto: '))

# Calcular o valor total
valor_total = preco_produto * quantidade_produto

# Exibir o resultado
print(f'Produto {nome_produto}\nPreço Unitário R${preco_produto:.2f}\nQuantidade {quantidade_produto}\nPreço Total R${valor_total}')