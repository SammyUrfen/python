t = int(input())
ans = list()

for _ in range(t):
    n = int(input())
    ans.append(format((n+n-1)/2, '.6f'))

for i in ans:
    print(i)
