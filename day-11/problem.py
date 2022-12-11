from math import lcm, prod


class Monkey(object):

    def __init__(self, id, items, operation, test, true_id, false_id):
        super(Monkey, self).__init__()
        self.id = id
        self.starting_item = tuple(items)
        self.items = items
        self.operation = operation
        self.test = test
        self.true_id = true_id
        self.false_id = false_id
        self.inspections = 0

    def inspect_and_throw(self, cap):
        self.inspections += len(self.items)
        inspected = [cap(self.operation(i)) for i in self.items]
        throw = {
            self.true_id: [i for i in inspected if self.test(i)],
            self.false_id: [i for i in inspected if not self.test(i)]
        }
        self.items.clear()
        return throw

    def reset(self):
        self.items = list(self.starting_item)
        self.inspections = 0


monkeys = [
    Monkey(0, [64], lambda i: i * 7, lambda i: i % 13 == 0, 1, 3),
    Monkey(1, [60, 84, 84, 65], lambda i: i + 7, lambda i: i % 19 == 0, 2, 7),
    Monkey(2, [52, 67, 74, 88, 51, 61], lambda i: i * 3, lambda i: i % 5 == 0, 5, 7),
    Monkey(3, [67, 72], lambda i: i + 3, lambda i: i % 2 == 0, 1, 2),
    Monkey(4, [80, 79, 58, 77, 68, 74, 98, 64], lambda i: i * i, lambda i: i % 17 == 0, 6, 0),
    Monkey(5, [62, 53, 61, 89, 86], lambda i: i + 8, lambda i: i % 11 == 0, 4, 6),
    Monkey(6, [86, 89, 82], lambda i: i + 2, lambda i: i % 7 == 0, 3, 0),
    Monkey(7, [92, 81, 70, 96, 69, 84, 83], lambda i: i + 4, lambda i: i % 3 == 0, 4, 5)
]


def run(iterations, cap):
    for m in monkeys:
        m.reset()
    for _ in range(iterations):
        for m in monkeys:
            thrown = m.inspect_and_throw(cap)
            for key, vals in thrown.items():
                monkeys[key].items.extend(vals)
    print(prod(sorted([m.inspections for m in monkeys])[-2:]))


# Part 1
run(20, lambda x: int(x / 3))
# 55216

# Part 2
mod = lcm(13, 19, 5, 2, 17, 11, 7, 3)
run(10000, lambda x: x % mod)
# 12848882750
