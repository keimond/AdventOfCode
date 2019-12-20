import re

data = []
zeros = {}
debug = False

image_x = 25
image_y = 6

with open('input', 'r') as f:
    try:
        data = next(f)
    except:
        pass

if debug:
    data = '123456789012'
    image_x = 3
    image_y = 2

images = {}
i=1

image_count = len(data) // image_x // image_y

pos = 0
for x in range(image_count):
    images.update({ x: []})
    for y in range(image_y):
        images[x].append(data[pos:pos + image_x])
        pos += image_x

count = image_x * image_y
lowest_image = 0

for x in images:
    zero_count = 0
    for y in images[x]:
        zero_count += len(re.sub("[1-9]", "", y))
    if zero_count < count:
        count = zero_count
        lowest_image = x

one_count = 0
two_count = 0

for x in images[lowest_image]:
    one_count += len(re.sub("[02-9]", "", x))
    two_count += len(re.sub("[013-9]", "", x))

print('Image #: {}'.format(lowest_image))
print('Answer: '.format(one_count * two_count))
print('Image Data: {}'.format(images[lowest_image]))
