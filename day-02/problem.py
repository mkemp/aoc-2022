with open('input') as f:
    lines = f.read().strip().split('\n')

# Part 1
# A, X = Rock
# B, Y = Paper
# C, Z = Scissors
table_1 = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3
}

total = 0
for line in lines:
    total += table_1[line]

print(total)
# 13809

# Part 2
# A = Rock
# B = Paper
# C = Scissors
# X = Lose
# Y = Draw
# Z = Win

table_2 = {
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 2 + 6,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6
}

total = 0
for line in lines:
    total += table_2[line]

print(total)
# 12316
