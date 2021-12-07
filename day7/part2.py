import pprint
f = open("input", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
data = [int(i) for i in data[0].split(",")]

result = {}
for x in range(2000):
    #print(x)
    fuel = 0
    for i in data:
        step = abs(x - i)
        fuel += step + (step*step-1/2)
        #fuel += step + sum([c for c in range(step)])
    result[x] = fuel
number = min(result, key=result.get)
print(result[number])
