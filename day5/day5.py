from collections import Counter

with open("input", "r") as f:
    lines = f.readlines()

coordinates = [tuple(map(int, tuple(i.strip().split(",")))) for line in lines for i in line.split('->')]
coordinates = [coordinates[i:i+2] for i in range(0, len(coordinates), 2)]

all_lines = []

def part_a():
    for coordinate_pair in coordinates:
        x1, y1 = coordinate_pair[0]
        x2, y2 = coordinate_pair[1]
        
        # Now calculate the points between the two points
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                all_lines.append((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                all_lines.append((x, y1))
        else:
            # If the points are not in a line, we need to calculate the points that are in the diagonal line of the points
            # and add them to the all_lines list
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if abs(x - x1) == abs(y - y1):
                        all_lines.append((x, y))

    # Count all interactions between the lines
    print(len([ x for x in list(Counter(all_lines).values()) if x > 1]))

part_a()