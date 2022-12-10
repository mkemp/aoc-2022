with open('input') as f:
    lines = f.read().strip().split('\n')

files = {}
folders = {''}
path = []

for line in lines:
    if line.startswith('$'):
        if line.startswith('$ cd'):
            name = line[5:]
            if name == '..':
                if len(path) > 0:
                    _ = path.pop(-1)
            elif name == '/':
                path = []
            else:
                path.append(name)
                folders.add('/'.join(path))
    else:
        val, key = line.split(' ')
        if val != 'dir':
            files['/'.join(path + [key])] = int(val)

folder_sizes = {
    path: sum(val for key, val in files.items() if key.startswith(path))
    for path in folders
}

# Part 1
target = 100000
print(sum(val for val in folder_sizes.values() if val <= target))
# 1582412

# Part 2
total = 70000000
needed = 30000000
available = total - folder_sizes['']
print(min(val for val in folder_sizes.values() if available + val >= needed))
# 3696336
