# Lista → estrutura que armazena vários valores
nomes = []  # cria uma lista vazia

# for → laço de repetição (repete várias vezes)
# range(5) → gera 5 repetições (0 até 4)
for i in range(5):
    nome = input("Digite um nome: ")  # recebe um nome (texto)
    
    # append() → adiciona um item dentro da lista
    nomes.append(nome)

print("Lista de nomes:")

# percorre (loop) todos os itens da lista
for nome in nomes:
    print(nome)  # imprime cada nome
