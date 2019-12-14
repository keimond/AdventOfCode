import ast

with open('input', 'r') as input:
    data = [int(i) for i in input.read().split(",")]

def add(in1, in2, out1):
    global data
    data[out1] = data[in1] + data[in2]

def multi(in1, in2, out1):
    global data
    data[out1] = data[in1] * data[in2]

pos = 0
while True:
    if data[pos] == 1:
        print("Position {0} is a {1}".format(pos,data[pos]))
        print("{0} + {1} to pos {2}".format(data[pos + 1],data[pos + 2],data[pos + 3]))
        add(data[pos + 1], data[pos + 2], data[pos + 3])
        pos = pos + 4
    elif data[pos] == 2:
        print("Position {0} is a {1}".format(pos,data[pos]))
        print("{0} * {1} to pos {2}".format(data[pos + 1],data[pos + 2],data[pos + 3]))
        multi(data[pos + 1], data[pos + 2], data[pos + 3])
        pos = pos + 4
    elif data[pos] == 99:
        print("Position {0} is a {1}".format(pos,data[pos]))
        break

print(data)