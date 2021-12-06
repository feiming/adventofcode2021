import pprint
import re
import pandas as pd

f = open("input", "r")
DATA = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
BOARD_SIZE = 1000

def get_x_y(data):
    _from,_to = data.split(" -> ")
    from_x,from_y = _from.split(",")
    to_x,to_y = _to.split(",")
    return int(from_x),int(from_y),int(to_x),int(to_y)

def swap(x1,x2):
    return x2,x1

#board = pd.DataFrame([[0]*BOARD_SIZE]*BOARD_SIZE)
board = pd.DataFrame([[0]*BOARD_SIZE]*BOARD_SIZE)

for i in DATA:
    from_x,from_y,to_x,to_y = get_x_y(i)
    print(f"from: {from_x},{from_y} to {to_x},{to_y}")
    if from_x == to_x:
        for y in range(min(from_y,to_y),max(from_y,to_y)+1):
            #print(f"{from_x},{y}")
            #print(f"before: {board[from_x][y]}")
            board[from_x][y] += 1
            #print(f"after: {board[from_x][y]}")
    elif from_y == to_y:
        for x in range(min(from_x,to_x),max(from_x,to_x)+1):
            #print(f"{x},{from_y}")
            #print(f"before: {board.loc[x][from_y]}")
            board[x][from_y] += 1
            #print(f"after: {board.loc[x][from_y]}")
    else:
        diff = abs(from_x - to_x)
        for i in range(0,diff+1):
            x_step = i
            y_step = i
            if from_x > to_x:
                x_step = -1 * i
            if from_y> to_y:
                y_step = -1 * i

            #print(f"{from_x+x_step},{from_y+y_step}")
            #print(f"before: {board[from_x+x_step][from_y+y_step]}")
            board[from_x+x_step][from_y+y_step] += 1
            #print(f"after: {board[from_x+x_step][from_y+y_step]}")

f = open("output", "w")
f.write(board.to_csv(sep=' ', index=False, header=False))

count = 0
for x in range(0,BOARD_SIZE):
    for y in range(0,BOARD_SIZE):
        if int(board[x][y]) > 1:
            count += 1

print(count)