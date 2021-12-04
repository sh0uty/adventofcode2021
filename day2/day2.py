items = []

with open("input", "r") as f:
    items += [line for line in f]

def part_a():
    position = {}
    position["forward"] = 0
    position["down"] = 0
    position["up"] = 0

    for i in range(len(items)):
        direction, number = items[i].split()
        position[direction] += int(number)
    print(position["forward"] * (position["down"] - position["up"]))
    

def part_b():
    depth = 0
    aim = 0
    horizontal = 0
    for i in range(len(items)):
        direction, number = items[i].split()
        if direction == "forward":
            horizontal += int(number)
            depth += aim * int(number)
        if direction == "up":
            aim -= int(number)
        if direction == "down":
            aim += int(number)
    print(horizontal * depth)

part_a()
part_b()