# int() → converte o valor digitado para número inteiro (sem casas decimais)

numero = int(input("Digite um número: "))  # recebe o número

# % → operador módulo (resto da divisão)
# numero % 2 → calcula o resto da divisão por 2

if numero % 2 == 0:  # if → estrutura condicional (SE)
    # == → operador de comparação (igual)
    print("O número é par")
else:  # else → SENÃO (caso não seja verdadeiro)
    print("O número é ímpar")
