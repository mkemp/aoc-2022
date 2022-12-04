from string import ascii_lowercase, ascii_uppercase

with open('input') as f:
    lines = f.read().strip().split('\n')

scores = {c: i + 1 for i, c in enumerate(ascii_lowercase + ascii_uppercase)}

# Part 1
total = 0
for line in lines:
    total += scores[list(set(line[:int(len(line) / 2)]) & set(line[int(len(line) / 2):]))[0]]

print(total)
# 8298

# Part 2
total = 0
for group in zip(lines[0::3], lines[1::3], lines[2::3]):
    total += scores[list(set(group[0]) & set(group[1]) & set(group[2]))[0]]

print(total)
# 2708
