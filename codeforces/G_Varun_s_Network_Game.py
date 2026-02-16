_, q = input().split(" ")
connected = set()

def union(a, b):
    city_a = set()
    city_b = set()
    for city in connected:
        if a and b in city:
            return None
        elif a in city:
            city_a = city
        elif b in city:
            city_b = city
        else:
            city_a.add(a)
            city_b.add(b)
    city = city_a.union(city_b)
    if city_a in connected:
        connected.remove(city_a)
    if city_b in connected:
        connected.remove(city_b)
    connected.add(city)

def find(a,b):
    for connects in connected:
        if a and b in connects:
            return "YES"
    return "NO"

for _ in range(int(7)):
    query = list(map(int, input().split(" ")))
    if query[0] == 1:
        union(query[1], query[2])
    else:
        ans = find(query[1], query[2])
        print(ans)