from itertools import takewhile

with open('input') as f:
    lines = f.read().strip().split('\n')
    trees = tuple(
        tuple(map(int, line))
        for line in lines
    )

max_x = len(trees[0])
max_y = len(trees)

# Part 1
visible = (max_x + max_y - 2) * 2
for x in range(1, max_x - 1):
    for y in range(1, max_y - 1):
        c = trees[y][x]
        if all([t < c for t in trees[y][:x]]) or \
                all([t < c for t in trees[y][x + 1:]]) or \
                all([t < c for t in (trees[j][x] for j in range(y))]) or \
                all([t < c for t in (trees[j][x] for j in range(y + 1, max_y))]):
            visible += 1

print(visible)
# 1823

# Part 2
max_scenic_score = 0
for x in range(1, max_x - 1):
    for y in range(1, max_y - 1):
        c = trees[y][x]
        up = len(tuple(takewhile(lambda j: 0 <= j and c > trees[j][x], range(y - 1, 0, -1)))) + 1
        down = len(tuple(takewhile(lambda j: j < max_y and c > trees[j][x], range(y + 1, max_y - 1)))) + 1
        left = len(tuple(takewhile(lambda i: 0 <= i and c > trees[y][i], range(x - 1, 0, -1)))) + 1
        right = len(tuple(takewhile(lambda i: i < max_x and c > trees[y][i], range(x + 1, max_x - 1)))) + 1
        score = up * down * left * right
        max_scenic_score = max(max_scenic_score, score)

print(max_scenic_score)
# 211680
