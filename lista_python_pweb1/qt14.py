input_list = input("Digite uma lista de números separados por espaço: ").split()
num_list = [int(num) for num in input_list]
num_list.sort(reverse=True)
print("Lista em ordem decrescente:", num_list)