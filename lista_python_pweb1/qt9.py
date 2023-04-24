numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()  # converte a string de entrada em uma lista de números
numeros = [float(numero) for numero in numeros]  # converte os elementos da lista para floats

soma = sum(numeros)
media = soma / len(numeros)

print("A média dos números é: ", media)