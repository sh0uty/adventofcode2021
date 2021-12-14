from collections import defaultdict

with open('input', 'r') as f:
    lines = [line.strip().split('-') for line in f.readlines()]


def find(current, visited, small, adjacent):
    if current in visited:
        return 0
    if current == 'end':
        return 1
    if current in small:
        visited.add(current)

    count = 0

    for next_node in adjacent[current]:
        count += find(next_node, visited, small, adjacent)

    visited.discard(current)

    return count

def find2(current, visited, small, adjacent, small_twice):
    if visited[current] > 0 and small_twice:
        return 0
    if current == 'end':
        return 1
    if current in small:
        visited[current] += 1
        if visited[current] == 2:
            small_twice = True

    count = 0

    for next_node in adjacent[current]:
        if next_node != 'start':
            count += find2(next_node, visited, small, adjacent, small_twice)

    visited[current] -= 1

    return count


def part_a():

    adjacent = defaultdict(list)
    small = set()

    for line in lines:
        a, b = line
        
        adjacent[a].append(b)
        adjacent[b].append(a)

        if a.lower() == a:
            small.add(a)
        if b.lower() == b:
            small.add(b)

    print(find('start', set(), small, adjacent))

def part_b():

    adjacent = defaultdict(list)
    small = set()

    for line in lines:
        a, b = line
        
        adjacent[a].append(b)
        adjacent[b].append(a)

        if a.lower() == a:
            small.add(a)
        if b.lower() == b:
            small.add(b)

    print(find2('start', defaultdict(int), small, adjacent, False))

part_a()
part_b()