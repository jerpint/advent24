
def load_data(file):
    with open(file) as f:
        data = f.readlines()

    # Add newline to make it easier to parse
    data = data + ["\n"]

    keys = []
    locks = []


    grid = []
    for idx, line in enumerate(data):
        line = line.strip("\n")

        if len(line) == 0:
            if grid[0][0] == "#":
                locks.append(grid)
            else:
                keys.append(grid)
            grid = []
            continue

        grid.append(line)

    return keys, locks



def get_lock_profile(lock):
    M = len(lock)
    N = len(lock[0])
    profile = []
    for j in range(N):
        for i in range(M):
            if lock[i][j] == ".":
                profile.append(i-1)
                break
    return profile


def get_key_profile(key):
    M = len(key)
    N = len(key[0])
    profile = []
    for j in range(N):
    #  for j in range(N-1, -1, -1):
        for i in range(M):
            if key[i][j] == "#":
                profile.append(6-i)
                break
    return profile


def check_fit(key, lock):
    for k, l in zip(key, lock):
        if k + l > 5:
            return False
    return True


#  file = "test.txt"
file = "input.txt"
keys, locks = load_data(file)

key_profiles = []
for key in keys:
    key_profiles.append(get_key_profile(key))

lock_profiles = []
for lock in locks:
    lock_profiles.append(get_lock_profile(lock))

fits = []
for key in key_profiles:
    for lock in lock_profiles:
        fits.append(check_fit(key, lock))


print(sum(fits))



