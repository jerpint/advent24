def load_data(file):
    with open(file) as f:
        data = f.readlines()

    values = {}

    for idx, line in enumerate(data):
        if line == "\n":
            break
        name, value = line.split(":")
        value = int(value)

        values[name] = value


    instructions = {}
    for line in data[idx+1:]:
        instruction, assignment = line.split("->")
        instructions[assignment.strip("\n").strip()] = instruction.strip()

    return values, instructions

def eval(v0, v1, op):


    if op == "AND":
        return v0 and v1

    elif op  == "OR":
        return v0 or v1

    elif op == "XOR":
        return v0 ^ v1

    else:
        raise ValueError("Unknown OP: ", op)



file = "input.txt"
values, instructions = load_data(file)

assignments = list(instructions.keys())
#  for assignment, inst in instructions.items():
while len(assignments) > 0:
    assignment = assignments.pop(0)

    inst = instructions[assignment]
    x0, op, x1  = inst.split()


    v0 = values.get(x0)
    v1 = values.get(x1)

    if v0 is not None and v1 is not None:
        values[assignment] = eval(v0, v1, op)
    else:
        assignments.append(assignment)


z_wires = {v: val for v, val in values.items() if v.startswith("z")}
z_wire_keys = sorted(z_wires.keys())[::-1]

bits = ""
for k in z_wire_keys:
    bits += str(values[k])

value = int(bits, 2)
print(value)




## Part 2


#  import copy
#
#  def get_val(letter, values):
#
#      letter_wires = {v: val for v, val in values.items() if v.startswith(letter)}
#      letter_wire_keys = sorted(letter_wires.keys())[::-1]
#
#      bits = ""
#      for k in letter_wire_keys:
#          bits += str(values[k])
#
#      value = int(bits, 2)
#
#      return value
#
#
#  def get_bits(letter, values):
#
#      letter_wires = {v: val for v, val in values.items() if v.startswith(letter)}
#      letter_wire_keys = sorted(letter_wires.keys())[::-1]
#
#      bits = ""
#      for k in letter_wire_keys:
#          bits += str(values[k])
#
#      return bits
#
#  def compute_instructions(values, instructions):
#      values = values.copy()
#      assignments = list(instructions.keys())
#      while len(assignments) > 0:
#          assignment = assignments.pop(0)
#
#          inst = instructions[assignment]
#          x0, op, x1  = inst.split()
#
#
#          v0 = values.get(x0)
#          v1 = values.get(x1)
#
#          if v0 is not None and v1 is not None:
#              values[assignment] = eval(v0, v1, op)
#          else:
#              assignments.append(assignment)
#
#
#
#      return values, instructions
#
#
#  def swap_instructions(k1, k2, instructions):
#      inst1 = instructions[k1]
#      inst2 = instructions[k2]
#
#      instructions[k1] = inst2
#      instructions[k2] = inst1
#
#      return instructions
#
#  def swap_2_instructions(swap1, swap2, instructions):
#      instructions = instructions.copy()
#
#      for swap in [swap1, swap2]:
#          k1, k2 = swap
#          instructions = swap_instructions(k1, k2, instructions)
#
#      return instructions
#
#
#  # Test part 1 still works
#  #  file = "test.txt"
#  #  values, instructions = load_data(file)
#  #  new_vals, new_inst = compute_instructions(values.copy(), instructions.copy())
#  #  z_val = get_val("z", new_vals)
#  #  print(z_val)
#
#  def compute_instructions_2(values, instructions):
#      values = values.copy()
#      assignments = list(instructions.keys())
#      count = 0
#      while len(assignments) > 0 and count < 1000:
#          count += 1
#          assignment = assignments.pop(0)
#
#          inst = instructions[assignment]
#          x0, op, x1  = inst.split()
#
#
#          v0 = values.get(x0)
#          v1 = values.get(x1)
#
#          if v0 is not None and v1 is not None:
#              values[assignment] = eval(v0, v1, op)
#          else:
#              assignments.append(assignment)
#
#      return values, instructions
#
#  #  file = "test2.txt"
#  file = "input.txt"
#  values, instructions = load_data(file)
#
#  x_val = get_val("x", values)
#  y_val = get_val("y", values)
#
#  x_bits = get_bits("x", values)
#  y_bits = get_bits("y", values)
#
#
#  swap_1 = ("z05", "z00")
#  swap_2 = ("z01", "z02")
#
#  new_inst = swap_2_instructions(swap_1, swap_2, instructions)
#  new_vals, new_inst = compute_instructions(values.copy(), new_inst.copy())
#  z_val = get_val("z", new_vals)
#  z_bits = get_bits("z", new_vals)
#
#  if x_val + y_val == z_val:
#      print("Good!")
#
#
#  def mega_brute_force_of_life():
#      k = list(instructions.keys())
#
#      for i in range(len(k)):
#          for j in range(i+1, len(k)):
#              swap_1 = (k[i], k[j])
#
#              k_remain = k.copy()
#              k_remain.remove(k[i])
#              k_remain.remove(k[j])
#
#              for ii in range(len(k_remain)):
#                  for jj in range(ii+1, len(k_remain)):
#                      print(jj)
#                      swap_2 = (k_remain[ii], k_remain[jj])
#
#                      print(swap_1)
#                      print(swap_2)
#
#                      new_inst = swap_2_instructions(swap_1, swap_2, instructions)
#                      new_vals, new_inst = compute_instructions_2(values.copy(), new_inst.copy())
#
#                      z_val = get_val("z", new_vals)
#                      z_bits = get_bits("z", new_vals)
#
#                      if x_val + y_val == z_val:
#                          print("Good!")
#                          return swap_1, swap_2
#
#  #  swap_1, swap_2 = mega_brute_force_of_life()
