# float() → usado pois valores podem ter casas decimais

capital = float(input("Digite o capital (C): "))  # dinheiro inicial
taxa = float(input("Digite a taxa (I): "))        # porcentagem
tempo = float(input("Digite o tempo (T): "))      # período

# Fórmula: J = (C * I * T) / 100
# * → multiplicação
# / → divisão
juros = (capital * taxa * tempo) / 100

print("O valor dos juros é:", juros)
