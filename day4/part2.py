import pprint
import re
import pandas as pd

f = open("input", "r")
#DATA = [x.rstrip("\n") for x in f]
DATA = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]

CALL = DATA.pop(0).split(",")

def check(cards,call):
    new_list = []
    for card in cards:
        try:
            not_bingo = True
            for i in range(5):
                # row
                if len(set(card.iloc[i].tolist()) & set(call)) == 5:
                    not_called = set(card.values.flatten()) - set(call)
                    print(f"not called: {not_called}")
                    last_call = call[-1]
                    print(f"last call: {last_call}")

                    sum = 0
                    for i in not_called:
                        sum += int(i)
                    sum = sum * int(last_call)
                    print(f"sum {sum}")
                    not_bingo = False
                    break
                    #return card
                # col
                if len(set(card[i].tolist()) & set(call)) == 5:
                    not_called = set(card.values.flatten()) - set(call)
                    print(f"not called: {not_called}")
                    last_call = call[-1]
                    print(f"last call: {last_call}")

                    sum = 0
                    for i in not_called:
                        sum += int(i)
                    sum = sum * int(last_call)
                    print(f"sum {sum}")
                    not_bingo = False
                    break
                    #return card
            if not_bingo:
                new_list.append(card)
        except Exception as e:
            print(e)

    return new_list

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
    cards = check(cards,CALL[0:i])
    print(f"cards left: {len(cards)}\n")
    if len(cards) == 0:
        break
    #data = check(cards,CALL[0:i])
    #if data is not None:
    #    if not data.empty:
    #        print(data)
    #        cards.remove(data)