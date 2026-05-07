print("Zadanie 1.4\n")
print("Nr1\n")
for j in range(10):
    if j%2 == 1:
        print(" ",end="")
    for i in range(10):       
        print('* ',end="")
    print()
print()
print("Nr2\n")
for j in range(1,5):
    for i in range(2):
        print("*" * j * 2)
print()
print("Nr3\n")
for i in range(6,0,-1):
    print("*" * i)