import pprint

f = open("file1", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]

x = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
]
for line in data:
    for i in range(len(line)):
        value = int(line[i])
        if value == 0:
            x[i][0] = x[i][0] + 1
        elif value == 1:
            x[i][1] = x[i][1] + 1

gamma = ""
epsilon = ""
for y in x:
    if y[0] > y[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
print(int(gamma, 2) * int(epsilon, 2))
