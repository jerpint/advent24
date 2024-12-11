with open("input.txt") as f:
    data = f.read()

#  with open("test.txt") as f:
#      data = f.read()

l1 = []
l2 = []
for line in data.split("\n"):
    if len(line.split("   ")) > 1:
        v1, v2 = line.split("   ")
        l1.append(int(v1))
        l2.append(int(v2))

total = 0
for n1, n2 in zip(sorted(l1), sorted(l2)):
    total += abs(n2 - n1)

print(total)

# Problem 2
def get_counts(l):
    counts = {}
    for num in l:
        counts[num] = counts.get(num, 0) + 1
    return counts


c2 = get_counts(l2)

total = 0
for n in l1:
    total += n * c2.get(n, 0)

print(total)

