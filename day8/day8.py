from functools import reduce

with open("test_input", "r") as f:
    lines = f.readlines()

def find(patterns, predicate):
    return next(pattern for pattern in patterns if predicate(pattern))

def solve():
    total = 0
    for line in lines:
        patterns, output = line.strip().split(" | ")

        patterns = [set(pattern) for pattern in patterns.split(" ")]
        output = [set(output) for output in output.split(" ")]

        solved = {}

        solved[1] = find(patterns, lambda digit: len(digit) == 2)
        solved[4] = find(patterns, lambda digit: len(digit) == 4)
        solved[7] = find(patterns, lambda digit: len(digit) == 3)
        solved[8] = find(patterns, lambda digit: len(digit) == 7)

        #for val in solved.values():
        #    for out in output:
        #        if val == out:
        #            total += 1
            


        unknown069 = [digit for digit in patterns if len(digit) == 6]
        solved[6] = find(unknown069, lambda digit: len(digit & solved[1]) == 1)
        solved[9] = find(unknown069, lambda digit: len(digit & solved[4]) == 4)
        solved[0] = find(unknown069, lambda digit: digit != solved[6] and digit != solved[9])

        unknown235 = [digit for digit in patterns if len(digit) == 5]
        solved[3] = find(unknown235, lambda digit: len(digit & solved[1]) == 2)
        solved[5] = find(unknown235, lambda digit: len(digit & solved[6]) == 5)
        solved[2] = solved[2] = find(unknown235, lambda digit: digit != solved[3] and digit != solved[5])

        total += reduce(lambda ans, digit: 10 * ans + list(solved.values()).index(digit), output, 0)
        
    return total

print(solve())