#!/bin/env python3

import math

total = float(0)

def getFuel(x):
  return math.floor(x / 3) - 2

with open('input', 'r') as file_input:
  for row in file_input:
    try:
      mass = float(row.rstrip('\n'))
      fuel = float(getFuel(mass))
      total = math.fsum([total, fuel])
    except:
      break

print(total)

