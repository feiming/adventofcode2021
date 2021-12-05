import pprint

f = open("file", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
horizontal = 0
depth = 0
aim = 0

for line in data:
    action, value = line.split(" ")
    print(f"action: {action}, value: {value}")
    if action == "up":
        print("up")
        aim -= int(value)
    elif action == "down":
        print("down")
        aim += int(value)
    elif action == "forward":
        print("forward")
        horizontal += int(value)
        depth += int(value) * int(aim)

    print(f"horizontal: {horizontal}")
    print(f"depth: {depth}")
    print(f"aim: {aim}\n")
print(depth * horizontal)
