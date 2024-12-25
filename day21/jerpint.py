def load_data(file):
    with open(file) as f:
        data = f.read()

    return [d for d in data.split("\n") if len(d) > 0]


def sign(x):
    return 1 if abs(x) == x else -1


class Keypad:
    def __init__(self):
        keypad = self.build_keypad()
        self.M = len(keypad)
        self.N = len(keypad[0])

        self.keypad = keypad


    def build_keypad(self):
        raise NotImplementedError()

    def get_pos(self, key: str):
        for i in range(self.M):
            for j in range(self.N):
                if self.keypad[i][j] == key:
                    return (i, j)
        raise ValueError(f"Key {key} not found")


    def get_distance(self, key_a: str, key_b: str):
        pos_a = self.get_pos(key_a)
        pos_b = self.get_pos(key_b)

        dx = pos_b[0] - pos_a[0]
        dy = pos_b[1] - pos_a[1]

        return (dx, dy)



    def __repr__(self):
        return "\n".join([str(k) for k in self.keypad])

    def pprint(self):
        print("\n".join([str(k) for k in self.keypad]))


    def find_sequence(self, key, next_key):
        """Finds the valid sequence between 2 key presses. Sequence returend is a string of button pushes."""

        start_pos = self.get_pos(key)

        if key == next_key:
            return ""

        distance = self.get_distance(key, next_key)


        X = distance[0]
        Y = distance[1]


        # Strategy is to always try going >>>>, ^^^^^ until reaching, or other way around
        # Keep track of the things you pass by, if you pass by an illegal move, then no good

        seq_1 = []  # Actual button presses
        pass_by_1 = []  # Keeps track of keys visited in sequence
        i, j = start_pos
        for dx in range(abs(X)):
            i += 1*sign(X)
            pass_by_1.append(self.keypad[i][j])
            seq_1.append("v" if sign(X) == 1 else "^")

        for dy in range(abs(Y)):
            j += 1*sign(Y)
            pass_by_1.append(self.keypad[i][j])
            seq_1.append(">" if sign(Y) == 1 else "<")

        #  if not None in pass_by:
        #      return "".join(sequence)

        seq_2 = []
        pass_by_2 = []
        i, j = start_pos
        for dy in range(abs(Y)):
            j += 1*sign(Y)
            pass_by_2.append(self.keypad[i][j])
            seq_2.append(">" if sign(Y) == 1 else "<")

        for dx in range(abs(X)):
            i += 1*sign(X)
            pass_by_2.append(self.keypad[i][j])
            seq_2.append("v" if sign(X) == 1 else "^")

        if None in pass_by_1:
            return "".join(seq_2)

        elif None in pass_by_2:
            return "".join(seq_1)

        # We have a tie-break, so compute the cost of pressing the first key and tie-break based on that
        cost = {
            "^": 0,
            ">": 0,
            "v": 1,
            "<": 2,
        }

        cost_1 = cost[seq_1[0]]
        cost_2 = cost[seq_2[0]]

        # I swear i thought this should be <= but can't figure out why its >=
        #  seq = seq_1 if cost_1 <= cost_2 else seq_2
        seq = seq_1 if cost_1 >= cost_2 else seq_2

        #  if cost_1 != cost_2:
        #      print(seq_1)
        #      print(seq_2)
        #      print(seq)
        #      print()

        return "".join(seq)


    def find_full_sequence(self, sequence: str):

        # A robot always points at the A key first
        start_key = "A"

        full_sequence = []
        key = start_key
        for next_key in sequence:
            full_sequence.append(self.find_sequence(key, next_key))
            key = next_key

        return "A".join(full_sequence) + "A"  # Account for each button press needed and final button press



class NumericKeypad(Keypad):
    def build_keypad(self):
        return [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, "0", "A"],
        ]


class DirectionalKeypad(Keypad):
    def build_keypad(self):
        return [
            [None, "^", "A"],
            ["<", "v", ">"],
        ]


def complexity(code, sequence):
    l = len(sequence)
    n = int(code.split("A")[0])

    print(l, n)

    return n*l

file = "input.txt"
#  file = "test.txt"
data = load_data(file)


dir_keypad = DirectionalKeypad()
num_keypad = NumericKeypad()

total = 0
for code in data:
    seq = num_keypad.find_full_sequence(code)

    #  print(code)
    #  print(seq)
    for _ in range(2):
        seq = dir_keypad.find_full_sequence(seq)
        #  print(seq)

    c = complexity(code, seq)
    total += c
    #  print(seq)

print(total)


## Part 2

# Simulating the whole process won't work, grows exponentially, must be more clever than that
