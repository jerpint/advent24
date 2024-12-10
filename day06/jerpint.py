from dataclasses import dataclass

file = "input.txt"
with open(file) as f:
    data = f.readlines()

grid = []
for line in data:
    line = line.strip("\n")
    grid.append(list(line))

M = len(grid)
N = len(grid[0])

@dataclass
class Position:
    i: int
    j: int
    direction: str

    def rotate_90(self):
        directions = ["^", ">", "v", "<"]
        new_idx = (directions.index(self.direction) + 1) % len(directions)
        self.direction = directions[new_idx]


    def is_in_bounds(self, grid):
        M = len(grid)
        N = len(grid[0])
        return self.i in range(M) and self.j in range(N)


def get_next_pos(position: Position):
    i, j, direction = position.i, position.j, position.direction
    if direction == "^":
        # Up
        i -= 1

    elif direction == "v":
        # Down
        i += 1

    elif direction == "<":
        # Left
        j -= 1

    elif direction == ">":
        # Right
        j += 1

    return Position(i, j, direction)

def get_start_pos(grid):

    M = len(grid)
    N = len(grid[0])

    for i in range(M):
        for j in range(N):
            if grid[i][j] == "^":
                return Position(i, j, "^")


def count_Xs(grid):
    total = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "X":
                total += 1
    return total


def pprint(grid, pos = None):

    grid_copy = grid.copy()

    if pos:
        # Print the current position
        grid_copy[pos.i][pos.j] = pos.direction

    grid_str = ""

    for line in grid_copy:
        grid_str += "".join(line)
        grid_str += "\n"

    print("*"*20)
    print()
    print(grid_str)
    print()
    print("*"*20)



pos = get_start_pos(grid)

grid[pos.i][pos.j] = "X"  # Mark starting point as visited
in_bounds = True
while in_bounds:
    #  pprint(grid, pos)
    next_pos = get_next_pos(pos)
    if next_pos.is_in_bounds(grid):

        if grid[next_pos.i][next_pos.j] in [".", "X"]:
            # Valid next mode, mark as visited and move
            grid[pos.i][pos.j] = "X"
            pos = next_pos
        else:
            # Otherwise, rotate
            pos.rotate_90()
    else:
        # Out of bounds, game over
        in_bounds = False
        grid[pos.i][pos.j] = "X"
        pos = None

#  pprint(grid, pos)
print(count_Xs(grid))


### Part 2

prev_grid = grid.copy()

def load_grid(file):
    with open(file) as f:
        data = f.readlines()

    grid = []
    for line in data:
        line = line.strip("\n")
        grid.append(list(line))

    return grid


def check_is_infinite(grid):

    pos = get_start_pos(grid)
    grid[pos.i][pos.j] = "X"  # Mark starting point as visited

    visited = set()  # Keep track of positions and orientations
    in_bounds = True
    infinite_loop = False
    while in_bounds and not infinite_loop:
        #  pprint(grid, pos)
        next_pos = get_next_pos(pos)
        if next_pos.is_in_bounds(grid):

            if grid[next_pos.i][next_pos.j] in [".", "X"]:
                # Valid next mode, mark as visited and move
                grid[pos.i][pos.j] = "X"
                pos = next_pos
            else:
                # Otherwise, rotate
                pos.rotate_90()


            set_pos = (pos.i, pos.j, pos.direction)
            if set_pos in visited:
                infinite_loop = True
            else:
                visited.add(set_pos)
        else:
            # Out of bounds, game over
            in_bounds = False
            grid[pos.i][pos.j] = "X"
            pos = None

    return infinite_loop

file = "input.txt"

# Load first to get stats
#  grid = load_grid(file)
M = len(grid)
N = len(grid[0])

# This is a very brute-force solution, takes long to run...
# For every point, place an obstacle, run the game, check if it gets stuck in infinite loop or not
# Surely, there must be a quicker way, but it works

total = 0
for i in range(M):
    for j in range(N):

        # Reset grid
        grid = load_grid(file)
        start_pos = get_start_pos(grid)


        if start_pos.i == i and start_pos.j == j:
            # Can't set obstacle on starting point, ignore
            continue

        if prev_grid[i][j] != "X":
            # It never passed by there, so we can ignore
            continue

        print(i, j)

        grid[i][j] = "O"  # Set Obstacle
        if check_is_infinite(grid):
            total += 1
print(total)
