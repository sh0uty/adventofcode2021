with open('input', 'r') as f:
    input_data = f.read()

coords, folds = input_data.split('\n\n')

coords = [tuple(map(int, c.split(','))) for c in coords.split('\n')]
folds = [tuple(f.split(' ')[-1].split('=')) for f in folds.split('\n')]

G = set(coords)
once = True
for fold in folds:
    newG = G.copy()
    if fold[0] == 'x':
        for c in G:
            if c[0] > int(fold[1]):
                newG.discard(c)
                newc = (2*int(fold[1]) - c[0], c[1])
                newG.add(newc)
    elif fold[0] == 'y':
        for c in G:
            if c[1] > int(fold[1]):
                newG.discard(c)
                newc = (c[0], 2*int(fold[1]) - c[1])
                newG.add(newc)
    G = newG

for y in range(max(G)[1] + 1):
    for x in range(max(G)[0] + 1):
        if (x, y) in G:
            print('#', end='')
        else:
            print('.', end='')
    print()