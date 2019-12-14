with open('input', 'r') as input:
    data = input.read().rstrip('\n').split('-')

range1 = list(data[0])
range2 = list(data[1])

fullrange = range(int(data[0]), int(data[1])+1)

#Test
#fullrange = ['111233', '332211', '223455', '123444', '400001', '111111', '223450', '123789', '122389', '212389', '445566']

rangeStep1 = []
rangeStep2 = []

def validateSeq(i):
    previous = -1
    myList = list(str(i))
    for num in myList:
        if int(num) >= previous:
            previous = int(num)
        else:
            return False
    return True

def validateSame(i):
    count,memory = 0,0
    myList = list(str(i))
    digit = myList[0]
    for num in myList[1:]:
        if num == digit:
            count += 1
        else:
            if count == 1:
                memory += 1
            count = 0
        digit = num
    if count == 1 and memory == 0:
        return True
    if memory > 0:
        return True
    return False

for x in fullrange:
    if validateSeq(x):
        rangeStep1.append(x)

for x in rangeStep1:
    if validateSame(x):
        rangeStep2.append(x)

print(len(rangeStep1))
print(len(rangeStep2))