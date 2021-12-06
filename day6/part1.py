import pprint
f = open("input", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
data = [int(i) for i in data[0].split(",")]

lanternfish = data
for i in range(256):
    newfish = []
    fishs = []
    for fish in lanternfish:
        fish -= 1
        if fish < 0:
            fishs.append(6)
            newfish.append(8)
        else:
            fishs.append(fish)
    fishs.extend(newfish)
    lanternfish = fishs
print(len(lanternfish))
