from scipy.spatial import distance
import json
import re

instructions,points = [],[]

## Set up two lists of instructions
with open('input', 'r') as file_input:
  for row in file_input:
    try:
      instructions.append(row.rstrip('\n').split(','))
    except:
      break

def addPoint(i,x,y):
    global points
    #points[i].append(x)
    #points[i].append(y)
    try:
        if points[i][x]:
            if y not in points[i][x]:
                points[i][x].append(y)
    except:
        points[i][x] = [y]

i = 0
for route in instructions:
    x, y = 0, 0
    points.append({})
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
p = 0
for i in range(int(len(intersections)/2)):
    md.append(distance.cityblock([0,0,0], [intersections[p],intersections[p+1],0]))
    p += 2

md.sort()
print(md[0])
