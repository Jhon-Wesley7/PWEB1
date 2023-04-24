numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()  
numeros = [int(numero) for numero in numeros] 

maior_numero = max(numeros)
menor_numero = min(numeros)

print("O maior número é: ", maior_numero)
print("O menor número é: ", menor_numero)