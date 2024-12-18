def load_data(file):
    with open(file) as f:
        data = f.readlines()
    coords = [line.strip("\n").split(",") for line in data]

    # swap i, j because this is easier for my brain at this point
    coords = [(int(j), int(i)) for i,j in coords]
    return coords


def build_grid(M, N, coords):
    grid = []
    for i in range(M):
        row = []
        for j in range(N):
            c = "." if (i,j) not in coords else "#"
            row.append(c)
        grid.append(row)
    return grid


def pprint(grid):
    grid_str = "\n".join(["".join(l) for l in grid])
    print(grid_str)


def pprint2(grid):


    new_grid = copy.deepcopy(grid)

    for i in range(M):
        for j in range(N):
            if isinstance(grid[i][j], tuple):
                new_grid[i][j] = "O"

    grid_str = "\n".join(["".join(l) for l in new_grid])
    print(grid_str)


def get_neighbours(pos, grid):
    directions = [(0,1), (1,0), (-1,0), (0, -1)]

    M = len(grid)
    N = len(grid[0])

    ns = []
    i, j = pos
    for dx, dy in directions:
        ni, nj = (i+dx, j+dy)
        if ni in range(M) and nj in range(N):
            if grid[ni][nj] != "#":
                ns.append((ni, nj))

    return ns


import copy

def bfs(grid):

    parents = copy.deepcopy(grid)

    start = (0, 0)
    q = []
    q.append(start)

    visited = set()

    count = 0
    while len(q) > 0:

        #  # Visualize grid filling up
        #  # So much fun!
        #  if count % 5 == 0:
        #      print()
        #      pprint2(parents)
        #      print()

        pos = q.pop(0)

        if pos in visited:
            continue

        ns = get_neighbours(pos, grid)
        for n in ns:
            if n not in visited:
                q.append(n)
                ni, nj = n
                parents[ni][nj] = (pos)

        visited.add(pos)
        #  print(len(visited))
        count += 1

    return parents


M, N = 7, 7
n_bytes = 12
file = "test.txt"

#  M, N = 71, 71
#  n_bytes = 1024
#  file = "input.txt"




coords = load_data(file)
grid = build_grid(M, N, coords[:n_bytes])

#  Run bfs, collect parents info
parents = bfs(grid)


shortest_grid = copy.deepcopy(grid)
shortest_path = []
next_ = (M-1,N-1)
while next_ != (0, 0):

    shortest_path.append(next_)
    i, j = next_
    shortest_grid[i][j] = "O"
    next_ = parents[i][j]

print(len(shortest_path))

# Visualize shortest path
#  pprint(shortest_grid)

## Part 2

def is_dead_end(coords, n_bytes, M, N):
    grid = build_grid(M, N, coords[:n_bytes])

    #  Run bfs, collect parents info
    parents = bfs(grid)

    return parents[M-1][N-1] == "."


def euler(coords, n_bytes):
    """Returns coord of first cause of dead end, use mid-point to swap out"""

    mid = len(n_bytes) // 2
    left = n_bytes[:mid]
    right = n_bytes[mid:]

    if len(n_bytes) == 1:
        return n_bytes[0] - 1  # Off by one because the last one left is still a dead end

    if is_dead_end(coords, left[-1], M, N):
        return euler(coords, left)
    else:
        return euler(coords, right)


M, N = 71, 71
n_bytes = 1024
file = "input.txt"

coords = load_data(file)
grid = build_grid(M, N, coords[:n_bytes])

n_bytes = list(range(len(coords)))
max_n_bytes = euler(coords, n_bytes)

i, j = coords[max_n_bytes]
print(f"{j},{i}") # Reverse it because we read coordinates in reverse at loading time
