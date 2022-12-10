from itertools import chain

with open('input') as f:
    lines = f.read().strip().split('\n')
    commands = list(chain.from_iterable(
        [direction] * int(magnitude)
        for direction, magnitude in (
            line.split(' ') for line in lines
        )
    ))

cmd_map = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

# Part 1
head = tail = (0, 0)
visited = {tail}
for cmd in commands:
    ix, iy = cmd_map[cmd]
    head = (head[0] + ix, head[1] + iy)
    dx, dy = head[0] - tail[0], head[1] - tail[1]
    if abs(dx) == 2 or abs(dy) == 2:
        tail = (tail[0] + min(1, max(-1, dx)), tail[1] + min(1, max(-1, dy)))
    visited.add(tail)

print(len(visited))
# 5981

# Part 2
rope = [(0, 0)] * 10
visited = {rope[-1]}
for cmd in commands:
    ix, iy = cmd_map[cmd]
    head = rope[0]
    rope[0] = (head[0] + ix, head[1] + iy)
    for i in range(1, len(rope)):
        dx, dy = rope[i - 1][0] - rope[i][0], rope[i - 1][1] - rope[i][1]
        if abs(dx) == 2 or abs(dy) == 2:
            rope[i] = (rope[i][0] + min(1, max(-1, dx)), rope[i][1] + min(1, max(-1, dy)))
    visited.add(rope[-1])

print(len(visited))
# 2352
