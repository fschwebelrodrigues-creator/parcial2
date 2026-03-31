# float() → permite trabalhar com números decimais

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# input() aqui recebe um TEXTO representando a operação (+, -, *, /)
operacao = input("Digite a operação (+, -, *, /): ")

# if / elif / else → estruturas condicionais
if operacao == "+":  # verifica se o usuário digitou "+"
    resultado = num1 + num2  # soma

elif operacao == "-":
    resultado = num1 - num2  # subtração

elif operacao == "*":
    resultado = num1 * num2  # multiplicação

elif operacao == "/":
    # verifica divisão por zero (não pode dividir por 0)
    if num2 != 0:  # != → diferente
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero")
        resultado = None  # None → valor vazio

else:
    print("Operação inválida")
    resultado = None

# só imprime se existir resultado válido
if resultado is not None:
    print("Resultado:", resultado)
    
