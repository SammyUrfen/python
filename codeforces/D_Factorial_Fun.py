n = int(input())

def calc(num):
    if num < 5:
        return 0
    else:
        return (num//5) + calc(num//5)

print(calc(n))
