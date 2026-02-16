c = input()
n = int(input())


for i in range(1, n+1):
    if i%4 == 1:
        print(c, end="")
    else:
        print(".", end="")
print()

for i in range(1, n+1):    
    if i%2 == 0:
        print(c, end="")
    else:
        print(".", end="")
print()

for i in range(3, n+3):
    if i%4 == 1:
        print(c, end="")
    else:
        print(".", end="")