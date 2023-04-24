lista_numeros = input("Digite uma lista de números separados por vírgula: ")
lista_numeros = lista_numeros.split(",") 
lista_numeros = [int(num) for num in lista_numeros] 
x = int(input("Digite o número que deseja verificar se está na lista: "))

if x in lista_numeros:
    print(f"O número {x} está presente na lista!")
else:
    print(f"O número {x} não está presente na lista.")