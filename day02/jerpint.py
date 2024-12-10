#  with open("test.txt") as f:
#      inputs = f.readlines()

with open("input.txt") as f:
    inputs = f.readlines()

def is_increasing_or_decreasing(data):
    sorted_data = sorted(data)
    if data[0] > data[-1]:
        return data == sorted_data[::-1]
    else:
        return data == sorted_data

def adjacency_check(data):
    for i in range(len(data)-1):
        abs_diff = abs(data[i] - data[i+1])
        if not (0 < abs_diff < 4):
            return False
    return True


def is_safe(data: list[str]) -> bool:
    return is_increasing_or_decreasing(data) and adjacency_check(data)

total = 0
for line in inputs:
    data = [int(i) for i in line.split(" ")]
    if is_safe(data):
        total += 1

print(total)


## Part 2
# ... just brute force it?

total = 0
for line in inputs:
    data = [int(i) for i in line.split(" ")]
    if is_safe(data):
        total += 1
    else:
        for i in range(len(data)):
            new_data = data.copy()
            new_data.pop(i)

            if is_safe(new_data):
                total += 1
                break

print(total)
