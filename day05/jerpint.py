with open("input.txt") as f:
    data = f.readlines()


def check_rule(pages: list[str], rule):
    page2idx = {p: idx for idx, p in enumerate(pages)}
    r0, r1 = rule
    idx0 = page2idx.get(r0)
    idx1 = page2idx.get(r1)

    if idx0 is None or idx1 is None:
        return True # "pass"

    return idx0 < idx1


def check_rules(pages, rules):
    for rule in rules:
        passes = check_rule(pages, rule)

        if not passes:
            return False

    return True


rules = []
page_numbers = []
for line in data:
    line = line.strip("\n")
    if "|" in line:
        r1, r2 = [int(r) for r in line.split("|")]
        rules.append((r1, r2))

    elif len(line) > 0:
        page_numbers.append([int(r) for r in line.split(",")])


total = 0
for pages in page_numbers:
    passes = check_rules(pages, rules)

    if passes:
        mid_idx = len(pages) // 2
        total += pages[mid_idx]

print(total)

## Part 2

def return_failing_rule(pages, rules):
    for rule in rules:
        passes = check_rule(pages, rule)

        if not passes:
            return rule

    return None


def update_pages(pages, failed_rule):
    "Swap the pages given the failed rule"
    page2idx = {p: idx for idx, p in enumerate(pages)}
    r0, r1 = failed_rule
    idx0 = page2idx.get(r0)
    idx1 = page2idx.get(r1)
    new_pages = pages.copy()
    new_pages[idx0] = r1
    new_pages[idx1] = r0
    return new_pages


def fix_pages(pages, rules):
    failed_rule = return_failing_rule(pages, rules)
    while failed_rule:
        pages = update_pages(pages, failed_rule)
        failed_rule = return_failing_rule(pages, rules)

    return pages



total = 0
for pages in page_numbers:
    passes = check_rules(pages, rules)

    if not passes:
        new_pages = fix_pages(pages, rules)
        mid_idx = len(pages) // 2
        total += new_pages[mid_idx]

print(total)
