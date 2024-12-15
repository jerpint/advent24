def load_data(file):
    with open(file) as f:
        data = f.readlines()

    positions = []
    velocities = []
    for line in data:
        _, p, v = line.split("=")

        p = [int(x.split()[0]) for x in p.split(",")]
        v = [int(x) for x in v.split(",")]

        positions.append(p)
        velocities.append(v)

    return positions, velocities

def move(n_seconds, pos, vel, W, H):
    x, y = pos
    vx, vy = vel
    new_x = (x + vx * n_seconds) % W
    new_y = (y + vy * n_seconds) % H

    return (new_x, new_y)


def construct_grid(positions, W, H):
    grid = [[0]*W for _ in range(H)]

    for pos in positions:
        x, y = pos
        grid[y][x] += 1

    return grid

def pprint(grid):

    import copy

    grid_copy = copy.deepcopy(grid)

    for y in range(H):
        for x in range(W):
            grid_copy[y][x] = str(grid_copy[y][x]) if grid_copy[y][x] != 0 else "."

    grid_str = "\n".join(["".join(g) for g in grid_copy])
    print(grid_str)


def get_safety_factor(grid, H, W):
    middle_x = W // 2
    middle_y = H // 2

    quadrants = [[0,0], [0,0]]

    for y in range(H):
        for x in range(W):
            if x < middle_x and y < middle_y:
                quadrants[0][0] += grid[y][x]
            if x > middle_x and y < middle_y:
                quadrants[1][0] += grid[y][x]

            if x < middle_x and y > middle_y:
                quadrants[0][1] += grid[y][x]
            if x > middle_x and y > middle_y:
                quadrants[1][1] += grid[y][x]


    return quadrants[0][0] * quadrants[0][1] * quadrants[1][1] * quadrants[1][0]

    pass

# Part one
file = "input.txt"
W, H = 101, 103
positions, velocities = load_data(file)
n_seconds = 100

new_positions = []
for pos, vel in zip(positions, velocities):
    new_pos = move(n_seconds, pos, vel, W=W, H=H)
    new_positions.append(new_pos)

grid = construct_grid(new_positions, W=W, H=H)
print(get_safety_factor(grid, H=H, W=W))

# Part two

import time

file = "input.txt"
W, H = 101, 103
positions, velocities = load_data(file)
grid = construct_grid(positions, W=W, H=H)

row_0 = grid[0]
row_1 = grid[1]
row_2 = grid[2]


new_positions = []
n_moves = 750+980+320+257+300+230+200+500+140+312+3297
for pos, vel in zip(positions, velocities):
    new_pos = move(n_moves, pos, vel, W=W, H=H)
    new_positions.append(new_pos)
    positions = new_positions
grid = construct_grid(positions, W=W, H=H)
#  pprint(grid)
print(n_moves)

# A bunch of code that was used for debugging!

#      grid = construct_grid(positions, W=W, H=H)

#  new_positions = []
#  for pos, vel in zip(positions, velocities):
#      new_pos = move(260+139+403+209+473, pos, vel, W=W, H=H)
#      new_positions.append(new_pos)
#      positions = new_positions

#  row_tip = [0]*W
#  #  row_tip[50] = 1
#
#  n_seconds = 1
#  for N in range(n_seconds):
#      new_positions = []
#      for pos, vel in zip(positions, velocities):
#          new_pos = move(1, pos, vel, W=W, H=H)
#          new_positions.append(new_pos)
#
#      positions = new_positions
#
#      grid = construct_grid(positions, W=W, H=H)
#
#      if row_0 == grid[0] and row_1 == grid[1] and row_2 == grid[2]:
#          print("Repeat!!!!???!?", N)
#          break
#
#      #  if row_tip == grid[0]:
#      #      print()
#      #      print(N)
#      #      pprint(grid)
#      #      print()
#
#      #  if N % 100 == 0:
#      #      print(N)
#      pprint(grid)
#      print(N)
#      print()
#      print()
#      time.sleep(0.001)
    #  print(get_safety_factor(grid, H=H, W=W))
