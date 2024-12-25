def load_data(file):
    with open(file) as f:
        data = f.read()

    return [int(n) for n in data.split("\n") if len(n) != 0]


def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

def evolve(secret):
    # Step 1
    secret = prune(mix(secret, secret * 64))

    # Step 2
    secret = prune(mix(secret, int(secret / 32)))

    # Step 3
    secret = prune(mix(secret, secret * 2048))

    return secret


def evolve_n_steps(secret, N):
    for n in range(N):
        secret = evolve(secret)
    return secret



file = "test.txt"
#  file = "input.txt"
data = load_data(file)
results = {secret: evolve_n_steps(secret, 2000) for secret in data}
print(sum(results.values()))


## Part 2

def get_price(secret):
    return int(str(secret)[-1])

def get_buying_info(secret, n_steps=2000):
    prices = [get_price(secret)]
    secrets = [secret]
    changes = [None]
    for _ in range(n_steps):
        secret = evolve(secret)
        secrets.append(secret)
        prices.append(get_price(secret))
        changes.append(prices[-1] - prices[-2])
    return secrets, prices, changes


def get_price_from_pattern(pattern, changes, prices):
    for idx in range(len(changes) - 3):
        if changes[idx:idx+4] == pattern:
            return prices[idx+3]
    return None


def get_max_patterns(changes, prices):
    patterns = []
    max_price = max(prices[5:])
    print(max_price)
    print()

    for idx in range(4, len(prices) - 3):
        if prices[idx] == max_price:
            pattern = tuple(changes[idx-3:idx+1])
            patterns.append(pattern)

    return patterns


def get_patterns_at(changes, prices, set_price):
    patterns = []

    for idx in range(4, len(prices) - 3):
        if prices[idx] == set_price:
            pattern = tuple(changes[idx-3:idx+1])
            patterns.append(pattern)

    return patterns


def get_all_patterns(changes):
    p = set()
    for idx in range(1, len(changes) - 4):
        p.add(tuple(changes[idx:idx+4]))
    return p




from collections import defaultdict
#  file = "test2.txt"
file = "input.txt"
data = load_data(file)

all_patterns = defaultdict(list)
all_prices = {}
all_changes = {}

for secret in data:
    secrets, prices, changes = get_buying_info(secret)
    #  max_patterns = set(get_max_patterns(changes, prices))
    #  max_patterns = set(get_patterns_at(changes, prices, 7))
    all_changes[secret] = changes
    all_prices[secret] = prices
    patterns = get_all_patterns(changes)
    #  all_patterns.append(p)
    for p in patterns:
        all_patterns[p].extend([secret])



pattern_counts = {p: len(s) for p, s in all_patterns.items()}
sorted_pattern_counts = sorted(list((pattern_counts.values())))[::-1]  # Sorted in ascending order

# 200 is kind of arbitrary, there was a bit of guessing and checking involved...
top_n_counts = sorted_pattern_counts[:200]

# Could speed it up by ordering in order of count
possible_patterns = [list(p) for p,c in pattern_counts.items() if c in top_n_counts]

max_bananas = 0
for pattern in possible_patterns:
    bananas = 0
    for secret in data:
        prices = all_prices[secret]
        changes = all_changes[secret]

        sell_price = get_price_from_pattern(pattern, changes, prices)
        if sell_price:
            bananas += sell_price

    if bananas >= max_bananas:
        #  print("New max: ", bananas)
        max_bananas = bananas
#
print(max_bananas)
