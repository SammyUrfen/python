n = int(input())
num = list(map(int, input().split(" ")))

maxm = max(num)
for i in range(maxm,0,-1):
    for ele in num:
        if ele >= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()