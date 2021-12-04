items = []

with open("input", "r") as f:
    items += [int(line) for line in f]

def part_a():
    print(sum([x1 < x2 for x1, x2 in zip(items, items[1:])]))

def part_b():
    zipped = list(zip(items, items[1:], items[2:]))
    print(sum([sum(zipped[i]) < sum(zipped[i+1]) for i in range(len(zipped) - 1)]))

part_a()
part_b()