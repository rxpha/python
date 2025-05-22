# Dados da viagem
distancia_percorrida = int(input('Digite a distância percorrida (em km): '))
combustivel_gasto = int(input('Digite o combustível gasto (em litros): '))

# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos dados
print("Dados da viagem:")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")