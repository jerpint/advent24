from copy import deepcopy


def load_data(file):
    with open(file) as f:
        raw_data = f.readlines()

    grid = []
    for line in raw_data:
        line = line.strip("\n")
        grid.append(list(line))
    return grid


def get_end_pos(grid):
    M = len(grid)
    N = len(grid[0])
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "E":
                return (i,j)


class UnvisitedSet:
    # There must definitely better data structures for this...
    def __init__(self, grid):

        self.visited = deepcopy(grid)
        self.values = []  # Store here the (min_value, pos, direction) where pos = (i,j) is position in grid

        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                self.visited[i][j] = False
                pos = (i, j)
                if grid[i][j] == "S":

                    self.values.append([0, pos, ">"])
                else:
                    self.values.append([float("inf"), pos, ""])


    def update_value(self, new_pos, new_val, new_dir):
        for idx, (val, pos, d) in enumerate(self.values):
            if new_pos == pos and new_val < val:
                self.values[idx] = [new_val, new_pos, new_dir]
                break

        self.sort_values()


    def get_value(self, pos):
        for (v, p, d) in self.values:
            if pos == p:
                return v


    def mark_visited(self, pos):
        i, j = pos
        self.visited[i][j] = True


    def sort_values(self):
        self.values.sort(key=lambda x: x[0])

    def get_min_unvisited(self):
        self.sort_values()
        for val, pos, d in self.values:
            i,j = pos
            if not self.visited[i][j] and val < float("inf"):
                return val, pos, d
        return "empty", "empty", "empty"


def pprint(grid):
    grid_str = "\n".join(["".join(str(l)) for l in grid])
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


def get_cost(pos, next_pos, direction):
    # Only valid if we are moving at most 1 neighbor away

    i, j = pos
    ni, nj = next_pos

    if (ni - i) > 0:
        intended_direction = "^"
    elif (ni - i) < 0:
        intended_direction = "v"
    elif (nj - j) > 0:
        intended_direction = ">"
    elif (nj - j) < 0:
        intended_direction = "<"
    else:
        raise ValueError("Debug?")

    if direction == intended_direction:
        cost = 1

    elif direction == "^" and intended_direction == "v":
        cost =  2001

    elif direction == "v" and intended_direction == "^":
        cost =  2001

    elif direction == ">" and intended_direction == "<":
        cost =  2001

    elif direction == "<" and intended_direction == ">":
        cost =  2001

    else:
        # Every other case involves a 90deg rotation
        cost = 1001

    return cost, intended_direction


file = "input.txt"
grid = load_data(file)
end_pos = get_end_pos(grid)
unvisited_set = UnvisitedSet(grid)

ei, ej = end_pos
while not unvisited_set.visited[ei][ej]:
    val, pos, d = unvisited_set.get_min_unvisited()
    ns = get_neighbours(pos, grid)


    for next_pos in ns:
        cost, next_dir = get_cost(pos, next_pos, d)
        unvisited_set.update_value(next_pos, val+cost, next_dir)

    unvisited_set.mark_visited(pos)

print(unvisited_set.get_value(end_pos))
