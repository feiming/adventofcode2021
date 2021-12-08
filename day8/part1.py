import pprint
f = open("input", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
data = [{"signal": i.split("|")[0].strip(), "output": i.split("|")[
    1].strip()} for i in data]

# pprint.pprint(data)
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count0 = 0
for x in data:
    output = x['output'].split(" ")
    print(output)
    number = ""
    for i in output:
        if len(i) == 7:
            count8 += 1
        elif len(i) == 4:
            count4 += 1
        elif len(i) == 3:
            count7 += 1
        elif len(i) == 2:
            count1 += 1
        elif i == "cdfbe":
            count5 += 1
        elif i == "gcdfa":
            count2 += 1
        elif i == "fbcad":
            count3 += 1
        elif i == "cefabd":
            count9 += 1
        elif i == "cdfgeb":
            count6 += 1
        elif i == "cagedb":
            count0 += 1


print(count1 + count4 + count7 + count8)
print(count1)
print(count4)
print(count7)
print(count8)
