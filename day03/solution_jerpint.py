import re
with open("input.txt") as f:
    data = f.read()

#  with open("test2.txt") as f:
#      data = f.read()

pattern = r"mul\([0-9]*,[0-9]*\)"
matches = re.findall(pattern, data)

total = 0
for match in matches:
    d1, d2 = match[4:-1].split(",")  # Drop 'mul(' and ')'
    d1, d2 = int(d1), int(d2)
    total += d1*d2
print(total)


## Part 2

pattern = r"don't\(\)|do\(\)|mul\([0-9]*,[0-9]*\)"
match_iters = re.finditer(pattern, data)

is_on = True
total = 0
for i in match_iters:
    if i.group() == "don't()":
        is_on = False
    elif i.group() == "do()":
        is_on = True
    elif is_on:
        d1, d2 = i.group()[4:-1].split(",")  # Drop 'mul(' and ')'
        d1, d2 = int(d1), int(d2)
        total += d1*d2


print(total)
