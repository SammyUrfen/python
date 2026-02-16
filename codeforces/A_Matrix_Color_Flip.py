n, m = input().split(" ")
red = 0
blue = 0
for _ in range(int(n)):
    rows = input()
    for colour in rows:
        if colour == "R":
            red += 1
        elif colour == "B":
            blue += 1

if red > blue :
    print(blue)
else:
    print(red)