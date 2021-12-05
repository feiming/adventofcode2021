import pprint
import re
import pandas as pd

f = open("input", "r")
#DATA = [x.rstrip("\n") for x in f]
DATA = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]

CALL = DATA.pop(0).split(",")

def check(cards,call):
    for card in cards:
        for i in range(5):
            # row
            if len(set(card.iloc[i].tolist()) & set(call)) == 5:
                not_called = set(card.values.flatten()) - set(call)
                print(not_called)
                last_call = call[-1]
                print(last_call)

                sum = 0
                for i in not_called:
                    sum += int(i)
                sum = sum * int(last_call)
                print(sum)
                return card
            # col
            if len(set(card[i].tolist()) & set(call)) == 5:
                not_called = set(card.values.flatten()) - set(call)
                print(not_called)
                last_call = call[-1]
                print(last_call)

                sum = 0
                for i in not_called:
                    sum += int(i)
                sum = sum * int(last_call)
                print(sum)
                return card

cards = []
for i in range(0,len(DATA),5):
    card = pd.DataFrame(
        [re.split(r' +', DATA[i].strip()),
        re.split(r' +', DATA[i+1].strip()),
        re.split(r' +', DATA[i+2].strip()),
        re.split(r' +', DATA[i+3].strip()),
        re.split(r' +', DATA[i+4].strip()),]
    )
    cards.append(card)

for i in range(0,len(CALL)):
    data = check(cards,CALL[0:i])
    if data is not None:
        if not data.empty:
            print(data)
            break