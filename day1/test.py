import pprint

f = open("file", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]


"""increase = 0
previous = 0
for x in data:
    if int(x) > int(previous):
        increase +=1
        print(f"{x} (increase)")
        print(increase)
    else:
        print(f"{x} (decrerase)")
    previous = x"""

increase = 0
index = 0
maximum = len(data)
for x in data:
    a1 = data[index] if index < maximum - 3 else 0
    a2 = data[index + 1] if index + 1 < maximum else 0
    a3 = data[index + 2] if index + 2 < maximum else 0
    a4 = data[index + 3] if index + 3 < maximum else 0
    sum1 = int(a1) + int(a2) + int(a3)
    sum2 = int(a2) + int(a3) + int(a4)
    print(f"{sum1} {sum2}")
    if sum2 > sum1:
        increase += 1
        print(f"{sum1} (increase)")
        print(increase)
    else:
        print(f"{sum1} (decrerase)")
    index += 1
