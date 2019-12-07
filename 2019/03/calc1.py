#!/usr/bin/env python3
import json
import re

routes,points = [],[]

## Set up two lists of instructions
with open('input', 'r') as file_input:
  for row in file_input:
    try:
      routes.append(row.rstrip('\n').split(','))
    except:
      break

i = 0
for route in routes:
    x, y = 0, 0
    points.append([])
    for instruction in route:
        # Extract direction and numbers from our value
        instruction = re.split('([A-Z])([0-9]+)', instruction)
        direction = instruction[1]
        distance = int(instruction[2])
        if direction == "U":
            y = y + distance + 1
            points[i].append(x)
            points[i].append(y)
        if direction == "D":
            y = y - distance + 1
            points[i].append(x)
            points[i].append(y)
        if direction == "R":
            x = x + distance + 1
            points[i].append(x)
            points[i].append(y)
        if direction == "L":
            x = x - distance + 1
            points[i].append(x)
            points[i].append(y)
    i =+ 1

print(points[0])
