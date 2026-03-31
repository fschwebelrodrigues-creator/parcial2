# int() → número inteiro (tempo geralmente sem casas decimais)

segundos = int(input("Digite o tempo em segundos: "))

# // → divisão inteira (descarta casas decimais)
horas = segundos // 3600  # 1 hora = 3600 segundos

# % → resto da divisão
resto = segundos % 3600  # sobra após tirar horas

minutos = resto // 60  # calcula minutos

seg = resto % 60  # segundos restantes

print("Tempo convertido:", horas, "h", minutos, "min", seg, "s")
