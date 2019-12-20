from __future__ import print_function
import re


data = []
zeros = {}
debug = False

image_x = 25
image_y = 6
images = {}

with open('input', 'r') as f:
    try:
        data = next(f)
    except:
        pass

if debug:
    data = ['0222','1122','2212','0000']

image_count = len(data) // image_x // image_y

pos = 0
for x in range(image_count):
    images.update({ x: []})
    for y in range(image_y):
        images[x].append(data[pos:pos + image_x])
        pos += image_x

for layer in images:
    image = ''
    for pixel in images[layer]:
        image += pixel
    images[layer] = image

decoded = list(images[0])

for x in images:
    if x != 0:
        for i,p in enumerate(str(images[x])):
            if re.match('^2$', decoded[i]) and re.match('^[01]$', p):
                decoded[i] = p

final = ''
for x in decoded:
  final += x

image = []
pos = 0
for y in range(image_y):
    image.append(final[pos:pos + image_x])
    pos += image_x

for row in image:
    for pixel in row:
        if pixel == '1':
            print("X", end='')
        if pixel == '0':
            print(" ", end='')
    print('')
