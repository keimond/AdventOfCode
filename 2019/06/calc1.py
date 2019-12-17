
data = []
arrayF = {}
arrayR = {}

with open('input', 'r') as input:
    try:
        while True:
            data.append(next(input).rstrip('\n').split(')'))
    except:
        pass
    
data.reverse()

for pair in data:
    arrayR.update({ pair[1]: pair[0] })

for k, v in arrayR.items():
    arrayF[v] = arrayF.get(v, [])
    arrayF[v].append(k)

# {'L': ['K'], 'K': ['J'], 'J': ['E'], 'I': ['D'], 'H': ['G'], 'G': ['B'], 'F': ['E'], 'E': ['D'], 'D': ['C'], 'C': ['B'], 'B': ['COM']}

print(arrayF)
print(arrayR)

l1,l2 = [],[]

for x in arrayR:
  l1.append(x)
  l2.append(arrayR[x])

ends = list(set(sorted(l1)) - set(sorted(l2)))

total = 0

def followChild(sat):
    global total
    previous = sat
    l = 0
    while l == 0:
        try:
            previous = arrayF[previous]
            total += 1
            for s in previous:
                print('found prev {}'.format(s))
                followChild(s)
        except:
            l = 1
            pass


def followPath(sat):
    print('called: {}'.format(sat))
    global arrayR,total
    if sat == 'COM':
        return False
    else:
        while True:
            if sat != 'COM':
                sat = arrayR[sat]
                total += 1
                followChild(sat)
            else:
                break
            

for i,x in enumerate(ends):
    followPath(x) 

print(total)

