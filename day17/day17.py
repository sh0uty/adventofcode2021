with open('test_input', 'r') as f:
    data = (f.readline().strip())[13:].split(', ')

target = [tuple(map(int, coords[2:].split('..'))) for coords in data]