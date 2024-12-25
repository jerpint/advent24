def load_data(file):
    with open(file) as f:
        data = f.readlines()

    nodes = []
    for line in data:
        line = line.strip("\n")
        (n1, n2) = line.split("-")

        nodes.append((n1, n2))
    return nodes


def get_connections(computer, all_nodes):
    connections = set()
    nodes = [node for node in all_nodes if computer in node]

    for node in nodes:
        #  n1, n2 = node
        for c in list(node):
            if c != computer:
                connections.add(c)

    return list(connections)

file = "test.txt"
#  file = "input.txt"
nodes = load_data(file)

# Build connections
all_nodes = []
all_computers = set()
for node in nodes:
    c1, c2 = node
    all_nodes.append(set(set((c1, c2))))
    all_computers.add(c1)
    all_computers.add(c2)


# We are pretty much brute forcing here
# Given a computer, find all its connections
# For each pair of connections, check if they are connected

all_three_nodes = set()
for c1 in all_computers:
    connections = get_connections(c1, all_nodes)

    for i in range(len(connections)):
        for j in range(i+1, len(connections)):
            c2 = connections[i]
            c3 = connections[j]

            if set((c2, c3)) in all_nodes:
                # Checks if they are connected

                trinode = [c1, c2, c3]
                trinode = tuple(sorted(trinode))
                all_three_nodes.add(trinode)


candidate_nodes = []
for node in all_three_nodes:
    for c in node:
        if c[0] == "t":
            candidate_nodes.append(node)
            break

print(len(candidate_nodes))


## Part 2

file = "input.txt"
#  file = "test.txt"
nodes = load_data(file)

# Build connections
all_nodes = []
all_computers = set()
for node in nodes:
    c1, c2 = node
    all_nodes.append(set(set((c1, c2))))
    all_computers.add(c1)
    all_computers.add(c2)

# This will be useful!
# https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique
# Basically a greedy algorithm


def get_clique(computer):
    clique = set()
    clique.add(computer)

    connections = get_connections(computer, all_nodes)

    for connection in connections:
        if connection == computer:
            # lazy way of skipping itself
            continue

        is_valid = True
        for c in clique:
            if not set((c, connection)) in all_nodes:
                is_valid = False
                break

        if is_valid:
            clique.add(connection)

    return clique

max_clique = set()
for computer in all_computers:
    clique = get_clique(computer)

    if len(clique) > len(max_clique):
        max_clique = clique
print(",".join(sorted(list(max_clique))))
