with open("input.txt") as f:
    raw_data = f.readlines()

data = []

for line in raw_data:
    data.append(list(line.strip("\n")))

M = len(data)
N = len(data[0])

targets = ["XMAS", "SAMX"]

## Part 1
total = 0
for i in range(M):
    for j in range(N):

        if j < N - 3:
            # Check horizontally
            line = data[i]
            if "".join(line[j:j+4]) in targets:
                total += 1

        if i < M - 3:
            # Check vertically
            to_check = [data[i+a][j] for a in range(4)]
            if "".join(to_check) in targets:
                total += 1

        # Check diagonally
        directions = [(0,0), (1,1),(2,2),(3,3)]
        to_check = ""
        for dx, dy in directions:
            if (i+dx) in range(M) and (j+dy) in range(N):
                to_check += data[i+dx][j+dy]

        if to_check in targets:
            total += 1

        # Check other diagonal
        directions = [(0,0), (-1,1),(-2, 2),(-3, 3)]
        to_check = ""
        for dx, dy in directions:
            if (i+dx) in range(M) and (j+dy) in range(N):
                to_check += data[i+dx][j+dy]

        if to_check in targets:
            total += 1


print(total)


## Part 2
targets = ["SAM", "MAS"]
total = 0
for i in range(M):
    for j in range(N):
        if data[i][j] == "A":
            dir1 = [(-1,-1), (0,0), (1,1)]
            to_check1 = ""
            for dx, dy in dir1:
                if (i+dx) in range(M) and (j+dy) in range(N):
                    to_check1 += data[i+dx][j+dy]

            dir2 = [(1,-1), (0,0), (-1,1)]
            to_check2 = ""
            for dx, dy in dir2:
                if (i+dx) in range(M) and (j+dy) in range(N):
                    to_check2 += data[i+dx][j+dy]

            if to_check1 in targets and to_check2 in targets:
                total += 1
print(total)
