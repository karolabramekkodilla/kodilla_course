num = 30
fibonacci = []

a = 1
b = 1

for i in range(num):
    fibonacci.append(a)

    next_number = a + b
    a = b
    b = next_number

print(fibonacci)