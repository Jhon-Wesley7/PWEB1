
input_list = input("Digite uma lista de números separados por espaço: ").split()

num_list = [int(num) for num in input_list]

num_list.sort()

print("Lista em ordem crescente:", num_list)