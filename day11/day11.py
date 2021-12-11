with open("input", "r") as f:
    lines = [list(map(int, line.strip())) for line in f.readlines()]


def flash(x, y):
    count = 1
    lines[x][y] = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if x+dx < 0 or x+dx >= len(lines) or y+dy < 0 or y+dy >= len(lines[x]) or lines[x+dx][y+dy] == 0:
                continue
            lines[x+dx][y+dy] += 1
            if lines[x+dx][y+dy] > 9:
                count += flash(x+dx, y+dy)
    return count

def solve():
    num_flashes = 0
    step = 0
    while True:
        new_flashes = 0
        if step == 100:
            print(f"part 1: {num_flashes}")
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                lines[x][y] += 1
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                if lines[x][y] > 9:
                    new_flashes += flash(x, y)
        num_flashes += new_flashes
        step += 1
        if new_flashes == 100:
            print(f"part 2: {step}")
            break

solve()