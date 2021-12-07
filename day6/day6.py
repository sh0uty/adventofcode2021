with open("input", "r") as f:
    initstate = list(map(int, f.readline().strip().split(",")))

def part_a():
    def simulate(days):
        for _ in range(days):
            for j in range(len(initstate)):
                if initstate[j] == 0:
                    initstate[j] = 6
                    initstate.append(8)
                else:
                    initstate[j] -= 1
    simulate(80)
    print(len(initstate))

# Optimize function part_a so it doesnt have to iterate through the entire list
def part_b():
    count = [initstate.count(i) for i in range(9)]
    for i in range(256):
        print(count)
        new = count.pop(0)
        count[6] += new
        count.append(new)
    print(sum(count))

part_b()