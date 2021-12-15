from heapq import heappush, heappop

with open('input') as f:
    Grid = [list(map(int, line.strip())) for line in f.readlines()]

def neighbours(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def bfs(G):
    queue = [(0, (0, 0))]
    finish = (len(G[0])-1, len(G)-1)
    visited = set()

    while queue:
        risk, pos = heappop(queue)

        if pos == finish:
            return risk

        if pos in visited:
            continue
        
        visited.add(pos)

        for x, y in neighbours(*pos):
            if 0 <= x < len(G) and 0 <= y < len(G[0]):
                heappush(queue, (risk + G[y][x], (x, y)))

print(f'Part 1: {bfs(Grid)}')


X = len(Grid[0])
Y = len(Grid)
X2 = X * 5
Y2 = Y * 5

Grid2 = [[0] * X2 for _ in range(Y2)]

for y in range(Y2):
    for x in range(X2):
        Grid2[x][y] = Grid[y % Y][x % X] + x // X + y // Y
        if Grid2[x][y] > 9:
            Grid2[x][y] -= 9
            
print(f'Part 2: {bfs(Grid2)}')
        