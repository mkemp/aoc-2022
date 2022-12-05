with open('input') as f:
    sections = f.read().strip().split('\n\n')
    # Not worth trying to parse this cleverly, just going to hard-code it.
    # [W] [V]     [P]
    # [B] [T]     [C] [B]     [G]
    # [G] [S]     [V] [H] [N] [T]
    # [Z] [B] [W] [J] [D] [M] [S]
    # [R] [C] [N] [N] [F] [W] [C]     [W]
    # [D] [F] [S] [M] [L] [T] [L] [Z] [Z]
    # [C] [W] [B] [G] [S] [V] [F] [D] [N]
    # [V] [G] [C] [Q] [T] [J] [P] [B] [M]
    #  1   2   3   4   5   6   7   8   9
    original_stacks = {
        1: 'VCDRZGBW',
        2: 'GWFCBSTV',
        3: 'CBSNW',
        4: 'QGMNJVCP',
        5: 'TSLFDHB',
        6: 'JVTWMN',
        7: 'PFLCSTG',
        8: 'BDZ',
        9: 'MNZW'
    }
    # We only care about the three numbers.
    commands = [
        (int(tokens[1]), int(tokens[3]), int(tokens[5])) for tokens in (
            line.split(' ') for line in sections[1].split('\n')
        )
    ]


# Part 1
stacks = original_stacks.copy()
for (n, f, t) in commands:
    for _ in range(n):
        stacks[f], stacks[t] = stacks[f][:-1], stacks[t] + stacks[f][-1]

print(''.join(v[-1] for v in stacks.values()))
# TBVFVDZPN

# Part 2
stacks = original_stacks.copy()
for (n, f, t) in commands:
    stacks[f], stacks[t] = stacks[f][:-n], stacks[t] + stacks[f][-n:]

print(''.join(v[-1] for v in stacks.values()))
# VLCWHTDSZ
