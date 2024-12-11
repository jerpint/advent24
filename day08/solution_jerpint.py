def load_data(file):
    with open(file) as f:
        raw_data = f.readlines()

    grid = []
    for line in raw_data:
        line = line.strip("\n")
        grid.append(list(line))
    return grid


def get_antennas(grid):

    M = len(grid)
    N = len(grid[0])

    antennas = {}
    for i in range(M):
        for j in range(N):
            if grid[i][j] != ".":
                a = grid[i][j]
                if antennas.get(a):
                    antennas[a].append((i,j))
                else:
                    antennas[a] = [(i,j)]
    return antennas


def get_next_nodes(a, b):

    # Get direction vector
    dx = b[0] - a[0]
    dy = b[1] - a[1]

    node_a = (a[0] - dx, a[1] - dy)  # Subtract from first node
    node_b = (b[0] + dx, b[1] + dy)  # Add to second node

    return node_a, node_b


def add_antinode(a, grid):
    M = len(grid)
    N = len(grid[0])
    i,j = a
    if i in range(M) and j in range(N):
        grid[i][j] = '#'


def count_antinodes(grid):
    M = len(grid)
    N = len(grid[0])

    total = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#':
                total += 1
    return total


def add_antinodes(a, b, grid):
    next_nodes = get_next_nodes(a,b)

    for node in next_nodes:
        add_antinode(node, grid)


grid = load_data("input.txt")
antennas = get_antennas(grid)

for freq in antennas:

    # Get all positions for a given freq.
    positions = antennas[freq]
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            # For each pair of antennas, add the antinodes
            a, b = positions[i], positions[j]
            add_antinodes(a, b, grid)

print(count_antinodes(grid))


## Part 2
def get_direction_vector(a, b):

    # Get direction vector
    dx = b[0] - a[0]
    dy = b[1] - a[1]

    return dx, dy


def is_in_bounds(node, grid):
    M = len(grid)
    N = len(grid[0])

    i, j = node

    return i in range(M) and j in range(M)

def add_antinodes(a, b, grid):
    dx, dy = get_direction_vector(a,b)

    next_node = (a[0] - dx, a[1] - dy)  # Subtract from first node
    while is_in_bounds(next_node, grid):
        add_antinode(next_node, grid)
        next_node = (next_node[0] - dx, next_node[1] - dy)

    next_node = (b[0] + dx, b[1] + dy)  # Add to second node
    while is_in_bounds(next_node, grid):
        add_antinode(next_node, grid)
        next_node = (next_node[0] + dx, next_node[1] + dy)


def count_antinodes(grid):
    M = len(grid)
    N = len(grid[0])

    total = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] != '.':
                # Antennas count too
                total += 1
    return total

grid = load_data("input.txt")
antennas = get_antennas(grid)


for freq in antennas:
    positions = antennas[freq]
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            a, b = positions[i], positions[j]
            add_antinodes(a, b, grid)
print(count_antinodes(grid))

def pprint(grid):
    grid_str = "\n".join(["".join(l) for l in grid])
    print(grid_str)
