with open('input') as f:
    lines = f.read().strip().split('\n')

# Part 1
cycles = {20, 60, 100, 140, 180, 220}
tick = 0
x = 1
signal = 0
for line in lines:
    for _ in range(1 if 'noop' == line else 2):
        tick += 1
        if tick in cycles:
            signal += x * tick
    if line.startswith('addx '):
        x += int(line[5:])

print(signal)
# 14820

# Part 2
pixels = []
tick = 0
x = 1
signal = 0
for line in lines:
    for _ in range(1 if 'noop' == line else 2):
        pixels.append('#' if x - 1 <= (tick % 40) <= x + 1 else '.')
        tick += 1
    if line.startswith('addx '):
        x += int(line[5:])

print('\n'.join([
    ''.join(pixels[:40]),
    ''.join(pixels[40:80]),
    ''.join(pixels[80:120]),
    ''.join(pixels[120:160]),
    ''.join(pixels[160:200]),
    ''.join(pixels[200:])
]))
# RZEKEFHA
