from collections import defaultdict, Counter

with open('input', 'r') as f:
    input_data = f.read()

poly, lines = input_data.split('\n\n')
translation = {l[0]:l[1] for l in [line.split(' -> ') for line in lines.split('\n')]}

elements = Counter(poly)
pairs = Counter(poly[i:i+2] for i in range(len(poly)-1))

for _ in range(40):
    new = Counter()
    for pair, digit in pairs.items():
        if pair in translation:
            a, b = pair
            c = translation[pair]
            new[a+c] += digit
            new[c+b] += digit
            elements[c] += digit  
        else:
            new[pair] += digit
    pairs = new
    if _ == 9:
        print(f'Part 1: {max(elements.values()) - min(elements.values())}')

print(f'Part 1: {max(elements.values()) - min(elements.values())}')