import heapq


class GridWithWeights(object):

    def __init__(self, grid):
        super(GridWithWeights, self).__init__()
        self.grid = grid
        self.cols = max(x for x, _ in grid.keys()) + 1
        self.rows = max(y for _, y in grid.keys()) + 1

    def cost(self, from_node, to_node):
        result = self.grid[to_node] - self.grid[from_node]
        return 1 if result <= 1 else 10000

    def neighbors(self, node):
        x, y = node
        if 0 <= x < self.cols and 0 <= y < self.rows:
            if 0 < x:
                yield (x - 1, y)
            if x < self.cols - 1:
                yield (x + 1, y)
            if 0 < y:
                yield (x, y - 1)
            if y < self.rows - 1:
                yield (x, y + 1)


class PriorityQueue(object):

    def __init__(self):
        super(PriorityQueue, self).__init__()
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(one, two):
    (x1, y1) = one
    (x2, y2) = two
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    # path.append(start) # optional, we don't count first node anyway
    # path.reverse() # optional, are just looking for the total cost
    return path


with open('input') as f:
    lines = f.read().strip().split('\n')

grid = {}
start, goal, lowest = None, None, ord('a')

for y, row in enumerate(lines):
    for x, val in enumerate(row):
        if val == 'S':
            val = 'a'
            start = (x, y)
        elif val == 'E':
            val = 'z'
            goal = (x, y)
        grid[(x, y)] = ord(val) - lowest

graph = GridWithWeights(grid)

# Part 1
came_from, cost_so_far = a_star_search(graph, start, goal)
# path = set([start] + reconstruct_path(came_from, start, goal))
# for y in range(graph.rows):
#   print(''.join(['X' if (x, y) in path else '.' for x in range(graph.cols)]))
print(len(reconstruct_path(came_from, start, goal)))
# 481


# Part 2
# Find valid starts that are next to a 'b'.
starts = set()
for x in range(graph.cols):
    for y in range(graph.rows):
        current = (x, y)
        if graph.grid[current] == 0:
            if any([graph.grid[node] == 1 for node in graph.neighbors(current)]):
                starts.add(current)

shortest = graph.rows * graph.cols
for start in starts:
    came_from, cost_so_far = a_star_search(graph, start, goal)
    shortest = min(shortest, len(reconstruct_path(came_from, start, goal)))

print(shortest)
# 480
