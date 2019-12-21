import ast

with open('input', 'r') as code:
    data = [int(i) for i in code.read().split(",")]
pos = 0
#test = '1002,4,3,4,33'
#data = test.split(",")

def add(pos1, pos2, pos3):
    global data
    data[pos3] = data[pos1] + data[pos2]

def multi(pos1, post2, post3):
    global data
    data[pos3] = data[pos1] * data[pos2]

def program(opcode, modes, parameters):
    global data,pos
    p = []
    print("op: {}, modes: {}, parameters: {}".format(opcode,modes,parameters))
    for i,m in enumerate(modes[:2]):
        if m == 0:
            p.append(int(data[parameters[i]]))
        else:
            p.append(int(parameters[i]))
    print(p)
    if opcode == 1:
        print('m=1')
        print('{} = {} + {}'.format(data[parameters[2]],p[0],p[1]))
        data[parameters[2]] = p[0] + p[1]
    if opcode == 2:
        print('m=2')
        print('{} = {} * {}'.format(data[parameters[2]],p[0],p[1]))
        data[parameters[2]] = p[0] * p[1]

while True:
    print('Position = {}'.format(pos))
    if data[pos] == 1:
        print('m=1')
        add(data[pos + 1], data[pos + 2], data[pos + 3])
        pos = pos + 4
    elif data[pos] == 2:
        print('m=2')
        multi(data[pos + 1], data[pos + 2], data[pos + 3])
        pos = pos + 4
    elif data[pos] == 3:
        print('m=3')
        IN = int(input("Enter the input value: "))
        i = data[pos + 1]
        data[i] = IN
        pos = pos + 2
    elif data[pos] == 4:
        print('m=4')
        i = data[pos +1]
        print(data[i])
        pos = pos + 2
    elif 4 <= len(str(data[pos])) <= 5:
        m = list(str(data[pos]))
        m.reverse()
        opcode = int(str(m[1]) + str(m[0]))
        m4 = 0
        if len(m) == 5:
            m4 = m[4]
        program(int(opcode), [int(m[2]),int(m[3]),int(m4)], [int(data[pos + 1]),int(data[pos + 2]),int(data[pos + 3])])
        pos = pos + 4
    elif data[pos] == 99:
        print("We were told to terminate at position {}".format(pos))
        break
    else:
        print("error.. can't handle {0}".format(data[pos]))
        quit(1)

print(data)
