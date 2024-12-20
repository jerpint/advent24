import time

def load_data(file):
    with open(file) as f:
        data = f.readlines()

    patterns = data[0].strip("\n").split(",")
    patterns = [p.strip(" ") for p in patterns]

    designs = []
    for line in data[2:]:
        designs.append(line.strip("\n"))
    return patterns, designs


def design_is_possible(design, patterns, checked = None, parents = None):

    if checked is None:
        checked = set()

    if design in patterns:
        return True

    to_check = []
    for p in patterns:
        if design.startswith(p):
            remainder = design[len(p):]
            #  print(p, remainder)
            to_check.append(remainder)

    for rem in to_check:
        if rem in checked:
            continue
        checked.add(rem)
        if design_is_possible(rem, patterns, checked):
            return True

    return False


### Below, a cemetery of different ideas and tries...

# Sort patterns from largest to smallest
#  patterns.sort(key=lambda x: len(x))
#  patterns = patterns[::-1]

#  def design_is_possible(design, patterns):
#      # For each large pattern, check if it contains it, remove it, then check if still possible
#      if design in patterns or design == "":
#          return True
#      #  all_possibles = []
#      for p in patterns:
#          if p in design:
#              r = re.search(p, design)
#              l, r = r.span()
#              left_design = design[:l]
#              right_design = design[r:]
#              print(p, left_design, right_design)
#              return design_is_possible(left_design, patterns) and design_is_possible(right_design, patterns)
#
#      return False



#  def design_is_possible(design, patterns):
#      # For each large pattern, check if it contains it, remove it, then check if still possible
#      if design in patterns or design == "":
#          return True
#      all_possibles = []
#      for p in patterns:
#          if p in design:
#              r = re.search(p, design)
#              l, r = r.span()
#              left_design = design[:l]
#              right_design = design[r:]
#              print(p, left_design, right_design)
#              all_possibles.append(design_is_possible(left_design, patterns) and design_is_possible(right_design, patterns))
#
#              if any(all_possibles):
#                  return True
#
#
#      return False


#  def design_is_possible(design, patterns):
#      # For each large pattern, check if it contains it, remove it, then check if still possible
#      if design in patterns:
#          return True
#      all_possibles = []
#      for p in patterns:
#          if p in design:
#              r = re.search(p, design)
#              l, r = r.span()
#              new_design = design[:l] + design[r:]
#              print(p, new_design)
#              all_possibles.append(design_is_possible(new_design, patterns))
#              if any(all_possibles):
#                  print(all_possibles)
#                  return True
#
#      print(all_possibles)
#      return any(all_possibles)

    #  return False


#  def design_is_possible(design, patterns):
#      # For each large pattern, check if it contains it, remove it, then check if still possible
#      if design in patterns:
#          return True
#      #  all_possibles = []
#      for p in patterns:
#          if p in design:
#              r = re.search(p, design)
#              l, r = r.span()
#              design = design[:l] + design[r:]
#              return design_is_possible(design, patterns)
#
#      return False

#  file = "test.txt"
#  file = "test2.txt"
file = "input.txt"
#  file = "test3.txt"
patterns, designs = load_data(file)



total = 0
for design in designs:
    candidates = [p for p in patterns if p in design]
    #  print(candidates)
    #  print(design)
    is_possible = design_is_possible(design, candidates)

    #  print()
    #  print()


    if is_possible:
        total += 1
    #  else:
    #      print(design, is_possible)

print(total)


## Part 2

def count_possibilities(design, patterns):

    if design in patterns:
        return 1

    to_check = []
    for p in patterns:
        if design.startswith(p):
            remainder = design[len(p):]
            #  print(p, remainder)
            to_check.append(remainder)

    totals = []
    for rem in to_check:
        totals.append(count_possibilities(rem, patterns))

    return sum(totals)



#  file = "input.txt"
#  #  file = "test.txt"
#  patterns, designs = load_data(file)
#  #
#  #
#  #
#  total = 0
#  for design in designs:
#      print(design)
#      candidates = [p for p in patterns if p in design]
#      if design_is_possible(design, candidates):
#          count = count_possibilities(design, candidates)
#      else:
#          count = 0
#      total += count
#      print(design, count)
#
#
#      #  else:
#      #      print(design, is_possible)
#
#  print(total)
