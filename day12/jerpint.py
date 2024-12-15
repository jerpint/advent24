def load_data(file):
    with open(file) as f:
        data = f.readlines()
    return [l.strip("\n") for l in data]


def get_neighbours(pos, grid):
    M = len(grid)
    N = len(grid[0])

    i, j = pos

    directions = [(0,1), (1,0), (-1,0), (0, -1)]

    n_positions = []
    n_values = []
    for dx, dy in directions:
        if (i+dx) in range(M) and (j+dy) in range(N):
            n_positions.append((i+dx,j+dy))
            n_values.append(grid[i+dx][j+dy])

    return n_positions, n_values


def get_perimeter(num_equal_neighbors: int):
    return 4 - num_equal_neighbors


def bfs(pos, grid):
    visited = set()
    queue = [pos]

    current_val = grid[pos[0]][pos[1]]
    total_area = 0
    total_perimeter = 0
    while len(queue) > 0:

        pos = queue.pop(0)

        if pos in visited:
            continue

        n_positions, n_values = get_neighbours(pos, grid)

        #  print(pos, grid[pos[0]][pos[1]])
        #  print(n_positions)
        #  print(n_values)

        num_equal_neighbors = 0
        for n_pos, n_val in zip(n_positions, n_values):
            if n_val == current_val:
                num_equal_neighbors += 1

                if n_pos not in visited:
                    queue.append(n_pos)

        visited.add(pos)

        total_area += 1
        total_perimeter += get_perimeter(num_equal_neighbors)

    price = total_area * total_perimeter
    print(f"Visited a region of {current_val} plants with price = {total_area}*{total_perimeter}={price}")
    return visited, price



grid = load_data("test.txt")

M = len(grid)
N = len(grid[0])

total_price = 0
visited = set()
for i in range(M):
    for j in range(N):
        pos = (i,j)
        if pos not in visited:

            next_visited, price = bfs(pos, grid)
            visited = visited.union(next_visited)
            total_price += price


print(total_price)


## Part two



def bfs(pos, grid):
    visited = set()
    queue = [pos]

    current_val = grid[pos[0]][pos[1]]
    total_area = 0
    total_perimeter = 0
    while len(queue) > 0:

        pos = queue.pop(0)

        if pos in visited:
            continue

        n_positions, n_values = get_neighbours(pos, grid)

        #  print(pos, grid[pos[0]][pos[1]])
        #  print(n_positions)
        #  print(n_values)

        num_equal_neighbors = 0
        for n_pos, n_val in zip(n_positions, n_values):
            if n_val == current_val:
                num_equal_neighbors += 1

                if n_pos not in visited:
                    queue.append(n_pos)

        visited.add(pos)

        #  total_area += 1
        #  total_perimeter += get_perimeter(num_equal_neighbors)

    #  price = total_area * total_perimeter
    #  print(f"Visited a region of {current_val} plants with price = {total_area}*{total_perimeter}={price}")
    return visited


grid = load_data("test.txt")

M = len(grid)
N = len(grid[0])

total_price = 0
visited = set()
for i in range(M):
    for j in range(N):
        pos = (i,j)
        if pos not in visited:

            next_visited = bfs(pos, grid)
            #  visited = visited.union(next_visited)
            #  total_price += price
            break


#  print(total_price)

def get_perimeter(visited):
    # Horizontal
    visited = list(next_visited)
    visited.sort(key=lambda x: x[0])

    # First and last coords
    i_min = visited[0][0]
    i_max = visited[-1][0]

    h_perimeter = 0
    for i in range(i_min, i_max+1):
        js = [v[1] for v in visited if v[0] == i]
        js.sort()

        h_perimeter += 1
        for idx in range(len(js)-1):
            if js[idx+1] - js[idx] != 1:
                h_perimeter += 1

    print(h_perimeter)

get_perimeter(next_visited)



