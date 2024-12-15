import numpy as np


def parse_block(block):

    # Parse button A
    A = block.split("\n")[0]
    _, ax, ay = A.split("+")
    ax = ax.split(",")[0]

    # Parse button B
    B = block.split("\n")[1]
    _, bx, by = B.split("+")
    bx = bx.split(",")[0]

    # Parse prize loc
    P = block.split("\n")[2]
    _, px, py = P.split("=")
    px = px.split(",")[0]

    ax, ay = int(ax), int(ay)
    bx, by = int(bx), int(by)
    px, py = int(px), int(py)
    return np.array([[ax, bx], [ay, by]]), np.array([[px], [py]])


def load_data(file):
    with open(file) as f:
        data = f.read()

    blocks = [parse_block(block) for block in data.split("\n\n")]
    return blocks





def solve_equation(W, Y):
    # Each block consists of W, Y matrices, we solve the question
    # X = W^-1 * Y
    X = (np.linalg.inv(W) @ Y)
    return X

def is_valid(a):
    return np.isclose(a, round(a)) and a <= 100


def solve(file):
    blocks = load_data(file)

    total = 0
    for block in blocks:
        W, Y = block
        X = solve_equation(W, Y)

        a, b = X[0][0], X[1][0]


        if is_valid(a) and is_valid(b):
            total += round(a)* 3 + round(b)*1

    print((total))

## Part 1
file = "input.txt"
solve(file)


## Part 2

def is_valid(a):
    return np.isclose(a, round(a), atol=0.01, rtol=0) and a >= 0

def solve_2(file, offset):
    blocks = load_data(file)

    total = 0
    for block in blocks:
        W, Y = block
        Y = Y + offset

        X = solve_equation(W, Y)

        a, b = X[0][0], X[1][0]

        if is_valid(a) and is_valid(b):
            total += round(a)* 3 + round(b)* 1

    print((total))



file = "input.txt"
offset = 10000000000000
solve_2(file, offset)
