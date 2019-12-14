import math

total = float(0)

def getFuel(x):
  return math.floor(x / 3) - 2

with open('input', 'r') as file_input:
  for row in file_input:
    try:
      mass = float(row.rstrip('\n'))
      fuel = float(getFuel(mass))
      while fuel > 0:
        total = math.fsum([total, fuel])
        fuel = float(getFuel(fuel))
    except:
      break

print(total)

