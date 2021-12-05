import pprint

f = open("file1", "r")
DATA = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]

data = DATA
oxygen = ""
for i in range(12):
    x = [0, 0]
    for line in data:
        value = int(line[i])
        if value == 0:
            x[0] = x[0] + 1
        elif value == 1:
            x[1] = x[1] + 1
    print(x)

    if x[0] > x[1]:
        oxygen += "0"
        data = [line for line in data if line[i] == "0"]
    else:
        oxygen += "1"
        data = [line for line in data if line[i] == "1"]
    print(oxygen)
    if len(data) == 1:
        oxygen = data[0]
        print(oxygen)
        break

data = DATA
co2 = ""
for i in range(12):
    x = [0, 0]
    for line in data:
        value = int(line[i])
        if value == 0:
            x[0] = x[0] + 1
        elif value == 1:
            x[1] = x[1] + 1
    print(x)

    if x[0] > x[1]:
        co2 += "1"
        data = [line for line in data if line[i] == "1"]
    else:
        co2 += "0"
        data = [line for line in data if line[i] == "0"]
    print(co2)
    if len(data) == 1:
        co2 = data[0]
        print(co2)
        break


print(int(co2, 2) * int(oxygen, 2))
