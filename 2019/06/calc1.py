data = []
satList = []
arrayR = {}
total = 0

with open('input', 'r') as input:
    try:
        while True:
            data.append(next(input).rstrip('\n').split(')'))
    except:
        pass
    
data.reverse()

for pair in data:
    arrayR.update({ pair[1]: pair[0] })

def followPath(sat):
    ltotal = 0
    global arrayR,total
    while sat != 'COM':
        ltotal += 1
        total += 1
        sat = arrayR[sat]

satList = []

for x in data:
    for y in x:
        if y not in satList and y != 'COM':
            satList.append(y)
    
for x in satList:
    followPath(x)

print('Total: {}'.format(total))
