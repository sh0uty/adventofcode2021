from collections import Counter
from collections import deque
from functools import reduce

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

openp = [ "(", "{", "[", "<" ]

closes = {}
closes['('] = ')'
closes['{'] = '}'
closes['['] = ']'
closes['<'] = '>'

value1 = {}
value1[')'] = 3
value1[']'] = 57
value1['}'] = 1197
value1['>'] = 25137

value2 = {}
value2[')'] = 1
value2[']'] = 2
value2['}'] = 3
value2['>'] = 4

def first_syntax_error(line):
    opens = deque()
    for char in line:
        if char in openp:
            opens.append(char)
        else:
            if char != closes[opens.pop()]:
                return char
    return None

def complete_parentesis(line):
    if first_syntax_error(line):
        return None
    opens = deque()
    for char in line:
        if char in openp:
            opens.append(char)
        else:
            opens.pop()
    solution = []
    while opens:
        solution.append(closes[opens.pop()])
    return solution

def part_a():
    score = 0
    for line in lines:
        if char := first_syntax_error(line):
            score += value1[char]
    print(score)

def part_b():
    scores = []
    for line in lines:
        solution = complete_parentesis(line)
        if not solution:
            continue
        scores.append(reduce(lambda ans, y: 5 * ans + y, [value2[char] for char in solution], 0))
    print(sorted(scores)[len(scores) // 2])

#part_a()
part_b()