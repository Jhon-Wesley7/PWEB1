n1 = int(input("Digite um numero: "))
fibonacci = [0,1]

for i in range (2, n1+1):
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    if next_fibonacci > n1:
        break
    fibonacci.append(next_fibonacci)

print("Sequência de fibonacci até {}: {}" .format(n1, fibonacci))    