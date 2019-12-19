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
    l = []
    while sat != 'COM':
        l.append(sat)
        sat = arrayR[sat]
    return(l)

l1 = followPath('YOU')
l2 = followPath('SAN')

for x in l1:
  if x in l2:
    match = x
  else:
    total += 1

for x in l2:
  if x in l1:
    break
  else:
    total += 1


print('Total: {}'.format(total - 2))
