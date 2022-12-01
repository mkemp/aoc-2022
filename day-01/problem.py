with open('input') as f:
    chunks = f.read().strip().split('\n\n')
    values = [sum(int(line) for line in chunk.split('\n')) for chunk in chunks]


# Part 1
print(max(values))
# 70720

# Part 2
print(sum(sorted(values, reverse=True)[:3]))
# 207148
