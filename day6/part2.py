import pprint

f = open("input", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
data = [int(i) for i in data[0].split(",")]
data.sort()
lanternfish = {
    0: len([i for i in data if i == 0]),
    1: len([i for i in data if i == 1]),
    2: len([i for i in data if i == 2]),
    3: len([i for i in data if i == 3]),
    4: len([i for i in data if i == 4]),
    5: len([i for i in data if i == 5]),
    6: len([i for i in data if i == 6]),
    7: len([i for i in data if i == 7]),
    8: len([i for i in data if i == 8]),
}

print(lanternfish)
for i in range(256):
    temp = lanternfish[0]
    lanternfish[0] = lanternfish[1]
    lanternfish[1] = lanternfish[2]
    lanternfish[2] = lanternfish[3]
    lanternfish[3] = lanternfish[4]
    lanternfish[4] = lanternfish[5]
    lanternfish[5] = lanternfish[6]
    lanternfish[6] = lanternfish[7] + temp
    lanternfish[7] = lanternfish[8]
    lanternfish[8] = temp
    print(lanternfish)

print(sum([i for i in lanternfish.values()]))