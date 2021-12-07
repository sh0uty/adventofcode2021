from statistics import median

with open("input", "r") as f:
    line = list(map(int, f.readline().split(",")))

def part_a():
    med = int(median(line))
    fuel = 0
    for item in line:
        fuel += abs(item-med)
    print(fuel)

def part_b():
    avg = int(sum(line)/len(line)) # Depending on your avg you maybe need to round it
    fuel = 0
    for item in line:
        fuel += sum([x for x in range(abs(item-avg)+1)])
    print(fuel)

#part_a()
part_b()