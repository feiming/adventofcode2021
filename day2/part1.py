import pprint

f = open("file", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
x = 0
y = 0

for line in data:
    action, value = line.split(" ")
    if action == "up":
        y -= int(value)
    elif action == "down":
        y += int(value)
    elif action == "forward":
        x += int(value)

print(x*y)
