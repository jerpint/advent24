def load_data(file):
    with open(file) as f:
        data = f.readlines()
    return [list(line.strip("\n")) for line in data]



def find_zeros(grid):
    M = len(grid)
    N = len(grid[0])

    positions = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "0":
                positions.append((i,j))
    return positions


def get_neighbors(grid, pos):
    M = len(grid)
    N = len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ns = []
    i, j = pos
    for dx, dy in directions:
        if (i+dx) in range(M) and (j+dy) in range(N):
            ns.append((i+dx, j+dy))
    return ns


def val_at_pos(grid, pos):
    i, j = pos
    return int(grid[i][j]) if grid[i][j] != "." else -100

def get_trailhead_score(grid, zero):
    """bfs algorithm."""
    score = 0

    i,j = zero
    q = [(i,j)]
    visited = set((i,j))

    while len(q) > 0:
        pos = q.pop(0)
        cur_val = val_at_pos(grid, pos)
        neighbors = get_neighbors(grid, pos)
        for n_pos in neighbors:
            n_val = val_at_pos(grid, n_pos)


            if (n_val - cur_val) == 1:
                q.append(n_pos)

                if n_val == 9 and n_pos not in visited:
                    score += 1
                    visited.add(n_pos)

    return score


grid = load_data("input.txt")
zeros = find_zeros(grid)

total = 0
for zero in zeros:
    total += get_trailhead_score(grid, zero)

print(total)


## Part 2

def get_trailhead_rating(grid, zero):
    """bfs algorithm."""
    score = 0

    i,j = zero
    q = [(i,j)]
    visited = set((i,j))

    while len(q) > 0:
        pos = q.pop(0)
        cur_val = val_at_pos(grid, pos)
        neighbors = get_neighbors(grid, pos)
        for n_pos in neighbors:
            n_val = val_at_pos(grid, n_pos)


            if (n_val - cur_val) == 1:
                q.append(n_pos)

                if n_val == 9:
                    score += 1

    return score


grid = load_data("input.txt")
zeros = find_zeros(grid)

total = 0
for zero in zeros:
    total += get_trailhead_rating(grid, zero)

print(total)
