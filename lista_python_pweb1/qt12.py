lista = input("Digite uma lista de números separados por vírgula: ")
numeros = lista.split(",")
soma = 0
for numero in numeros:
    soma += int(numero)
print("A soma dos números é:", soma)