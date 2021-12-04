from collections import Counter

items = []

with open("test_input", "r") as f:
    items += [line.strip() for line in f]

def part_a():
    #create a dict with the keys 1 and 0 and set the values to 0
    gamma = ''
    epsilon = ''
    for j in range(len(items[0])):
        diagnistic = {'1':0, '0':0}
        for i in range(len(items)):
            diagnistic[items[i][j]] += 1
        gamma += str(max(diagnistic, key=diagnistic.get))
        epsilon += str(min(diagnistic, key=diagnistic.get)) 
    print(int(gamma, 2) * int(epsilon, 2))

def part_a_2():
    gamma = int(''.join([Counter(x).most_common(1)[0][0] for x in zip(*items)]), 2)
    epsilon = int(len(items[0]) * '1', 2) - gamma
    print(gamma * epsilon)

def part_b():
    print(int(part_b1(), 2) * int(part_b2(), 2))

def part_b1():
    oxygen = ''
    new_items = items.copy()
    for j in range(len(new_items[0])):
        diagnistic = {'1':0, '0':0}
        for i in range(len(new_items)):
            diagnistic[new_items[i][j]] += 1
        oxygen += str(max( diagnistic, key=diagnistic.get ))
        new_items = [x for x in new_items if x.startswith(oxygen)]
        if len(new_items) == 1:
            return new_items[0]
        
def part_b2():
    scrubber = ''
    new_items = items.copy()
    for j in range(len(new_items[0])):
        diagnistic = {'1':0, '0':0}
        for i in range(len(new_items)):
            diagnistic[new_items[i][j]] += 1
        scrubber += '0' if diagnistic['1'] >= diagnistic['0'] else '1'
        new_items = [x for x in new_items if x.startswith(scrubber)]
        if len(new_items) == 1:
            return new_items[0]


#part_a()
part_a_2()

#part_b()