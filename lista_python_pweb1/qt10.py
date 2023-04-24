numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()  
numeros = [int(numero) for numero in numeros]  

print("Números pares na lista: ")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)