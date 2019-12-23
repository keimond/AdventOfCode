from scipy.spatial import distance
import json
import re

instructions,points,steps = [],[],[]

## Set up two lists of instructions
with open('input', 'r') as file_input:
  for row in file_input:
    try:
      instructions.append(row.rstrip('\n').split(','))
    except:
      break

def addPoint(i,x,y):
    global points,steps,s
    s += 1
    #print('{},{},{},{}'.format(i,x,y,s))
    try:
        if steps[i][x]:
            try:
                if steps[i][x][y]:
                    pass
            except:
                steps[i][x].update({ y: s })
    except:
        steps[i][x] = { y: s }
    try:
        if points[i][x]:
            if y not in points[i][x]:
                points[i][x].append(y)
    except:
        points[i][x] = [y]

i = 0
for route in instructions:
    s, x, y = 0, 0, 0
    points.append({})
    steps.append({})
    for instruction in route:
        # Extract direction and numbers from our value
        instruction = re.split('([A-Z])([0-9]+)', instruction)
        direction = instruction[1]
        dist = int(instruction[2])
        if direction == "U":
            for d in range(dist):
                y = y + 1
                addPoint(i,x,y)
        if direction == "D":
            for d in range(dist):
                y = y - 1
                addPoint(i,x,y)
        if direction == "R":
            for d in range(dist):
                x = x + 1
                addPoint(i,x,y)
        if direction == "L":
            for d in range(dist):
                x = x - 1
                addPoint(i,x,y)
    i =+ 1

intersections=[]
for x in points[0]:
    for y in points[0][x]:
        try:
            if y in points[1][x]:
                intersections.append(x)
                intersections.append(y)
        except:
            pass

md = []
sl = []
p = 0
for i in range(int(len(intersections)/2)):
    x = intersections[p]
    y = intersections[p+1]
    s1 = steps[0][x][y]
    s2 = steps[1][x][y]
    sl.append(s1 + s2)
    md.append(distance.cityblock([0,0,0], [x,y,0]))
    p += 2

md.sort()
sl.sort()
print(sl[0])
