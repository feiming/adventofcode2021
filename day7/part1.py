import pprint
f = open("input", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
data = [int(i) for i in data[0].split(",")]

result = {}
for x in range(2000):
    fuel = 0
    for i in data:
        fuel += abs(x - i)
    result[x] = fuel
print(min(result, key=result.get))
print(result[316])