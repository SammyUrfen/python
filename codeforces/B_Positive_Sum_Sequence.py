n = input()
sqnc = list(map(int, input().split(" ")))

sum = 0
num = max(sqnc)

if num > 0:
    for no in sqnc:
        if no > 0:
            sum += no

else:
    sum = num

print(sum)