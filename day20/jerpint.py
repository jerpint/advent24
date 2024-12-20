import copy

def load_data(file):
    with open(file) as f:
        raw_data = f.readlines()

    grid = []
    for line in raw_data:
        line = line.strip("\n")
        grid.append(list(line))
    return grid


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


    M = len(grid)
    N = len(grid[0])
    new_grid = copy.deepcopy(grid)

    for i in range(M):
        for j in range(N):
            if isinstance(grid[i][j], tuple):
                new_grid[i][j] = "O"

    print(new_grid)
    #  try:
    grid_str = "\n".join(["".join(l) for l in new_grid])
    #  except:
    #      import ipdb; ipdb.set_trace();

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


def get_symbol_pos(grid, s):
    M = len(grid)
    N = len(grid[0])

    for i in range(M):
        for j in range(N):
            if grid[i][j] == s:
                return (i,j)



def bfs(grid):

    parents = copy.deepcopy(grid)

    #  start = (0, 0)
    start_pos = get_symbol_pos(grid, "S")
    end_pos = get_symbol_pos(grid, "E")

    q = []
    q.append(start_pos)

    visited = set()

    count = 0
    while len(q) > 0 and end_pos not in visited:

        #  # Visualize grid filling up
        #  # So much fun!
        #  if count % 500 == 0:
        #      print()
        #      pprint2(parents)
        #      print()

        pos = q.pop(0)

        if pos in visited:
            continue

        ns = get_neighbours(pos, grid)
        #  print(ns)
        for n in ns:
            if n not in visited:
                q.append(n)
                ni, nj = n
                parents[ni][nj] = (pos)

        visited.add(pos)
        #  print(len(visited))
        count += 1

    return parents


def get_len_shortest_path(grid):
    #  Run bfs, collect parents info
    parents = bfs(grid)


    # Build back the shortest path
    shortest_grid = copy.deepcopy(grid)
    shortest_path = []
    end_pos = get_symbol_pos(grid, "E")
    start_pos = get_symbol_pos(grid, "S")
    next_ = end_pos
    while next_ != start_pos:

        shortest_path.append(next_)
        i, j = next_
        shortest_grid[i][j] = "O"
        next_ = parents[i][j]

    #  print(len(shortest_path))
    return len(shortest_path), shortest_path



def get_all_shortest_paths(grid, shortest_path):
    # We know that the cheat must be distance 2 and land back on the shortest path
    # Iterate through all points on shortest path, compute 2 in each direction, and see which lands back on shortest
    # path


    directions = [(0, 1), (1,0), (0, -1), (-1, 0)]


    valid_cheat_positions = set()
    all_shortest_paths = []
    shortest_path = shortest_path[::-1]  # Reverse it for easier logic, start_pos is now first
    #  shortest_path = [shortest_path[0]] + shortest_path  # Add the start position so we can consider it too

    start_idx = get_symbol_pos(grid, "S")
    print(start_idx)

    # Start idx not included originally
    shortest_path = [start_idx] + shortest_path


    for pos in shortest_path:
        for dx, dy in directions:
            i, j = pos
            cheat_1x, cheat_1y = i+dx, j+dy
            cheat_2x, cheat_2y = i+2*dx, j+2*dy
            cheat_1 = (cheat_1x, cheat_1y)
            cheat_2 = (cheat_2x, cheat_2y)

            if cheat_2 in shortest_path: # Check that we land back on the track
                cheat_2_idx = shortest_path.index(cheat_2)
                pos_idx = shortest_path.index(pos)
                if cheat_2_idx > pos_idx: # Make sure we're ahead, not behind, otherwise doesn't make sense

                    grid_val1 = grid[cheat_1x][cheat_1y]
                    grid_val2 = grid[cheat_2x][cheat_2y]

                    if grid_val1 == "#" or grid_val2 == "#":  # Make sure we're actually using the cheat

                        #  if (cheat_1, cheat_2) and (cheat_2, cheat_1) not in valid_cheat_positions:  # Avoid permutations, i don tthink this is necessary though
                        valid_cheat_positions.add((cheat_1, cheat_2))
                        new_shortest_path = shortest_path[:pos_idx] + [cheat_1, cheat_2] + shortest_path[cheat_2_idx:]

                        all_shortest_paths.append(new_shortest_path[1:]) # Remove the added start pos for consistency



    return all_shortest_paths, valid_cheat_positions

# Load data
file = "test.txt"
#  file = "input.txt"
grid = load_data(file)

# First calculate the normal path length
normal_path_len, shortest_path = get_len_shortest_path(grid)

all_shortest_paths, cheat_positions = get_all_shortest_paths(grid, shortest_path)

#  print(len(cheat_positions)) # Should be equal to 43 for test input

# Visualize all cheat positions on grid to see if we did it well
#  for c1, c2 in cheat_positions:
#      grid_copy = copy.deepcopy(grid)
#      i, j = c1
#      grid_copy[i][j] = "1"
#      i, j = c2
#      grid_copy[i][j] = "2"
#      print()
#      pprint2(grid_copy)


counts = {}
for idx, path in enumerate(all_shortest_paths):


    shortest_path_len =  len(path)
    time_saved = normal_path_len - shortest_path_len
    counts[time_saved] = counts.get(time_saved, 0) + 1

total = 0
for time_saved, count in counts.items():
    print(f"There are {count} cheats that save {time_saved} picoseconds.")

    if time_saved >= 100:
        total += count

print(total)


## Part 2


def get_all_shortest_paths(grid, shortest_path):
    # We know that the cheat must be distance 2 and land back on the shortest path
    # Iterate through all points on shortest path, compute 2 in each direction, and see which lands back on shortest
    # path


    directions = [(0, 1), (1,0), (0, -1), (-1, 0)]


    valid_cheat_positions = set()
    all_shortest_paths = []
    shortest_path = shortest_path[::-1]  # Reverse it for easier logic, start_pos is now first

    start_idx = get_symbol_pos(grid, "S")
    print(start_idx)

    # Start idx not included originally
    shortest_path = [start_idx] + shortest_path


    c_len = 2  # Cheat length
    for pos in shortest_path:
        for dx, dy in directions:
            i, j = pos
            cheat_1x, cheat_1y = i+dx, j+dy
            cheat_2x, cheat_2y = i+c_len*dx, j+c_len*dy
            cheat_1 = (cheat_1x, cheat_1y)
            cheat_2 = (cheat_2x, cheat_2y)

            if cheat_2 in shortest_path: # Check that we land back on the track
                cheat_2_idx = shortest_path.index(cheat_2)
                pos_idx = shortest_path.index(pos)
                if cheat_2_idx > pos_idx: # Make sure we're ahead, not behind, otherwise doesn't make sense

                    grid_val1 = grid[cheat_1x][cheat_1y]
                    grid_val2 = grid[cheat_2x][cheat_2y]

                    if grid_val1 == "#" or grid_val2 == "#":  # Make sure we're actually using the cheat

                        #  if (cheat_1, cheat_2) and (cheat_2, cheat_1) not in valid_cheat_positions:  # Avoid permutations, i don tthink this is necessary though
                        valid_cheat_positions.add((cheat_1, cheat_2))
                        new_shortest_path = shortest_path[:pos_idx] + [cheat_1, cheat_2] + shortest_path[cheat_2_idx:]

                        all_shortest_paths.append(new_shortest_path[1:]) # Remove the added start pos for consistency



    return all_shortest_paths, valid_cheat_positions
