from functools import reduce

with open("input", "r") as f:
    heightmap = [list(map(int, x.strip())) for x in f.readlines()]

mins = []

def adjacent_cells_are_bigger(x, y):
    adjacent_bigger = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0) or (x + i < 0) or (y + j < 0) \
                or (x + i >= len(heightmap)) or (y + j >= len(heightmap[0])):
                continue
            adjacent_bigger.append(heightmap[x + i][y + j] >= heightmap[x][y])
    return all(adjacent_bigger)

def part_a():
    risk = 0
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            if adjacent_cells_are_bigger(x, y):
                risk += heightmap[x][y] + 1
                mins.append((x, y))
    print(risk)


def flood(i, j, seen):
    if i < 0 or i >= len(heightmap) or j < 0 or j >= len(heightmap[0]) \
        or heightmap[i][j] == 9 or (i, j) in seen:
        return 
    seen.add((i, j))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        flood(i+dx, j+dy, seen)

def part_b():
    basins = []
    for m in mins:
        seen = set()
        flood(*m, seen)
        basins.append(seen)
    top3 = sorted(basins, key=lambda x: len(x))[-3:]
    print(reduce(lambda x, y: x * len(y), top3, 1))

part_a()
part_b()