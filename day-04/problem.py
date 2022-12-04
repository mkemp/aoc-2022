with open('input') as f:
    lines = f.read().strip().split('\n')


def parse_ranges(line):
    l, _, r = line.partition(',')
    return tuple(map(int, l.split('-'))), tuple(map(int, r.split('-')))


ranges = [
    parse_ranges(line) for line in lines
]

# Part 1
count = 0
for (l_min, l_max), (r_min, r_max) in ranges:
    if (l_min <= r_min and r_max <= l_max) or (r_min <= l_min and l_max <= r_max):
        count += 1

print(count)
# 562

# Part 2
count = 0
for (l_min, l_max), (r_min, r_max) in ranges:
    if (l_min <= r_min <= l_max) or (l_min <= r_max <= l_max) or (r_min <= l_min <= r_max) or (r_min <= l_max <= r_max):
        count += 1

print(count)
# 924
