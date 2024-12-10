def parse_data(file):
    with open(file) as f:
        raw_data = f.readlines()

    # Read and parse the data
    data = []
    for line in raw_data:
        line = line.strip("\n")
        target, nums = line.split(":")
        target = int(target)
        nums = [int(num) for num in nums.split()]
        data.append((target, nums))
    return data


def compute(a, b, op):
    """Compute given the op"""
    if op == "+":
        return a + b
    if op == "*":
        return a * b


def check_seq(nums, target, seq):
    total = nums[0]
    for i in range(len(seq)):
        b = nums[i+1]
        op = seq[i]

        total = compute(total, b, op)

        if total > target:
            # Dead-end
            return -1

    # Check that we equal target and use all nums
    return total == target and len(seq) == len(nums) - 1


def bfs(target, nums, ops):
    q = ops.copy()
    dead_ends = set()

    while len(q) > 0:
        #  print(q)
        #  print(dead_ends)
        seq = q.pop(0)

        if seq in dead_ends:
            break

        check = check_seq(nums, target, seq)

        #  print(nums, target, seq, check)

        if check == -1:
            dead_ends.add(seq)
            continue

        elif check == True:
            return True

        else:
            if len(seq) < len(nums)-1:
                for op in ops:
                    q.append(seq+op)

    return False

data = parse_data(file="input.txt")
ops = ["+", "*"]
total = 0
for target, nums in data:

    result = bfs(target, nums, ops)
    print("*"*20)
    print(target, nums)
    print("Result:", result)
    print("*"*20)

    if result:
        total += target

print(total)

## Part 2

def compute(a, b, op):
    """Compute given the op"""
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "|":
        return int(str(a) + str(b))
    else:
        raise ValueError(f"Op {op} Unknown")



ops = ["+", "*", "|"]
data = parse_data(file="input.txt")
total = 0
for target, nums in data:

    result = bfs(target, nums, ops)
    print("*"*20)
    print(target, nums)
    print("Result:", result)
    print("*"*20)

    if result:
        total += target

print(total)
