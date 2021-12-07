import pprint
f = open("input", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
data = [int(i) for i in data[0].split(",")]

data.sort()
crab = {}
for i in data:
    if i in crab:
        crab[i] += 1
    else:
        crab[i] = 1
pprint.pprint(crab)