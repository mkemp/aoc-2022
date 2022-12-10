with open('input') as f:
    line = f.read().strip()


def find_marker(line, marker_len):
    for i in range(len(line)):
        if len(set(line[i:i + marker_len])) == marker_len:
            print(i + marker_len)
            break


# Part 1
marker_len = 4
find_marker(line, marker_len)
# 1912

# Part 2
marker_len = 14
find_marker(line, marker_len)
# 2122
