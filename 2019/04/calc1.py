#!/usr/bin/env python3

with open('input', 'r') as input:
    data = input.read().rstrip('\n').split('-')

range1 = list(data[0])
range2 = list(data[1])

fullrange = range(int(data[0]), int(data[1])+1)

#Test
#fullrange = ['400001', '111111', '223450', '123789', '122389', '212389', '445566']

rangeStep1 = []
rangeStep2 = []

def validateSame(i):
    previous,count = -1,0
    myList = list(str(i))
    for num in myList:
        if int(num) == previous:
            count += 1
        else:
            previous = int(num)
    if count: return True
    else: return False

def validateSeq(i):
    previous = -1
    myList = list(str(i))
    for num in myList:
        if int(num) >= previous:
            previous = int(num)
        else:
            return False
    return True

for x in fullrange:
    if validateSame(x):
        rangeStep1.append(x)

for x in rangeStep1:
    if validateSeq(x):
        rangeStep2.append(x)

print(len(rangeStep1))
print(len(rangeStep2))

