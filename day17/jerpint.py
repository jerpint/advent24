from ast import literal_eval
def load_data(file):
    with open(file) as f:
        data = f.readlines()

    registers = {}
    for line in data:
        line = line.strip("\n")
        if "A" in line:
            registers["A"] = int(line.split(" ")[-1])
        if "B" in line:
            registers["B"] = int(line.split(" ")[-1])
        if "C" in line:
            registers["C"] = int(line.split(" ")[-1])

        if "Program" in line:
            program = [int(c) for c in line.split(" ")[-1].split(",")]

    return registers, program


class Computer:
    def __init__(self, registers, program):
        self.OPS = {
                0: "adv",
                1: "bxl",
                2: "bst",
                3: "jnz",
                4: "bxc",
                5: "out",
                6: "bdv",
                7: "cdv",
            }
        self.registers = registers
        self.program = program
        self.instruction_pointer = 0
        self.outputs = []


    def combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.registers["A"]
        elif operand == 5:
            return self.registers["B"]
        elif operand == 6:
            return self.registers["C"]
        elif operand == 7:
            raise ValueError("Reserved!")
        else:
            raise ValueError("Unknown")



    def adv(self, operand):
        combo = self.combo(operand)
        numerator = self.registers["A"]
        denominator = 2 ** combo
        self.registers["A"] = int(numerator / denominator)

    def bxl(self, operand):
        self.registers["B"] = self.registers["B"] ^ operand

    def bst(self, operand):
        self.registers["B"] = self.combo(operand) % 8

    def jnz(self, operand):
        if self.registers["A"] == 0:
            return

        self.instruction_pointer = operand - 2

    def bxc(self, operand):
        self.registers["B"] = self.registers["B"] ^ self.registers["C"]


    def out(self, operand):
        combo = self.combo(operand)
        self.outputs.append(combo % 8)

    def bdv(self, operand):
        combo = self.combo(operand)
        numerator = self.register["A"]
        denominator = 2 ** combo
        self.registers["B"] = int(numerator / denominator)

    def cdv(self, operand):
        combo = self.combo(operand)
        numerator = self.registers["A"]
        denominator = 2 ** combo
        self.registers["C"] = int(numerator / denominator)

    def evaluate(self, instruction, operand):
        op = self.OPS[instruction]


        if op == "adv":
            return self.adv(operand)

        elif op == "bxl":
            return self.bxl(operand)

        elif op == "bst":
            return self.bst(operand)

        elif op == "jnz":
            return self.jnz(operand)

        elif op == "bxc":
            return self.bxc(operand)

        elif op == "out":
            return self.out(operand)

        elif op == "bdv":
            return self.bdv(operand)

        elif op == "cdv":
            return self.cdv(operand)

        else:
            raise ValueError(f"Uknown op: {op}")


    def get_next_instruction_and_operand(self):
        instruction, operand = self.program[self.instruction_pointer], self.program[self.instruction_pointer+1]
        return instruction, operand
    def step(self):

        while self.instruction_pointer < len(program):
            inst, operand = self.get_next_instruction_and_operand()
            self.evaluate(inst, operand)
            self.instruction_pointer += 2

        #  print("Halt")
        #  print("Outputs: ", ",".join([str(out) for out in self.outputs]))
        return self.outputs




registers, program = load_data("input.txt")

#  print(registers, program)
computer = Computer(registers.copy(), program)
outputs = computer.step()

print(",".join([str(out) for out in outputs]))


## Part 2

# Tried Brute force, ran all night, didnt produce an answer.
# Halt program as soon as output not equal program
# There's probably a smarter way...

class Computer2(Computer):
    def step(self):

        while self.instruction_pointer < len(program):
            inst, operand = self.get_next_instruction_and_operand()
            self.evaluate(inst, operand)
            self.instruction_pointer += 2

            if len(self.outputs) > 0:
                for out, prog in zip(self.outputs, self.program):
                    if out != prog:
                        return

        #  print("Halt")
        #  print("Outputs: ", ",".join([str(out) for out in self.outputs]))
        return self.outputs

registers, program = load_data("input.txt")


#  A = 4063000000  Reached here with brute force
A = 0
while True:
    if A % 100000 == 0:
        print(A)
    input_registers = registers.copy()
    input_registers["A"] = A
    computer = Computer2(input_registers, program)
    outputs = computer.step()

    if outputs == program:
        print("DONE")
        break

    else:
        A += 1

print(A)
