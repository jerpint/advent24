def load_data(file):
    with open(file) as f:
        return f.read().strip("\n")


def generate_blocks(disk_map):
    blocks = []
    for idx, i in enumerate(disk_map):

        if idx % 2:
            blocks.extend( ["."]*int(i))
        else:
            blocks.extend( [str(idx // 2)] *int(i))

    return blocks


def get_next_valid_block_from_end(end: int, blocks):
    for j in range(end, -1, -1):
        if blocks[j] != ".":
            return j


def compact_blocks(blocks):
    #  blocks = list(blocks)
    end = get_next_valid_block_from_end(len(blocks) - 1, blocks)
    for idx, block in enumerate(blocks):

        if end == idx:
            break

        if block == ".":
            blocks[idx] = blocks[end]
            blocks[end] = "."
            end = get_next_valid_block_from_end(end, blocks)

        #  print("".join(blocks))

    return blocks

def compute_checksum(blocks):
    checksum = 0
    for idx, num in enumerate(blocks):
        if num == ".":
            return checksum
        checksum += idx*int(num)
    return checksum


disk_map = load_data("input.txt")
blocks = generate_blocks(disk_map)
compact_blocks = compact_blocks(blocks)
print(compute_checksum(compact_blocks))


## Part two

def generate_blocks(disk_map):
    blocks = []
    for idx, i in enumerate(disk_map):

        if idx % 2:
            if int(i) > 0:
                blocks.append( ["."]*int(i))
        else:
            blocks.append( [str(idx // 2)] *int(i))

    return blocks


def get_free_space_map(blocks):
    free_space_map = []
    pos = 0
    for idx, block in enumerate(blocks):

        if block[0] == ".":
            free_space_map.append((idx, len(block)))

        pos += len(block)

    return free_space_map


def get_next_valid_block_from_end(blocks):
    for idx, block in enumerate(blocks[::-1]):
        if block[0] != ".":
            block_idx = len(blocks) - idx - 1
            return block, block_idx


def pprint(blocks):
    print("".join(["".join(b) for b in blocks]))


def move_block_at_fileid(blocks, file_id: int):

    free_space_map = get_free_space_map(blocks)
    #  block = blocks[block_idx]
    for idx, block in enumerate(blocks):
        if block[0] != "." and block[0] == str(file_id):
            block_idx = idx
            break

    K = len(block)
    for free_block_idx, free_len in free_space_map:

        if free_len > K and free_block_idx < block_idx:
            # First condition means we have more space than needed
            # Second condition ensures we Only move forward in queue, not backwards
            blocks[free_block_idx] = ["."] * (free_len - len(block))  # Remaining free memory after insert
            blocks.insert(free_block_idx, block)  # Insert at index
            blocks[block_idx + 1] = ["."] * K  # Overwrite at end (+1 because we added a new index)
            return True

        elif free_len == K and free_block_idx < block_idx:
            # First condition means we have just enough space
            # Second condition ensures we Only move forward in queue, not backwards
            blocks[free_block_idx] = block
            blocks[block_idx] = ["."] * K
            return True

    return False


def compute_checksum(blocks):
    blocks_ext = [b for block in blocks for b in block]
    checksum = 0
    for idx, num in enumerate(blocks_ext):
        if num == ".":
            continue

        checksum += idx*int(num)
    return checksum


def get_max_file_id(blocks):
    for block in blocks[::-1]:
        if block[0] != ".":
            max_file_id = int(block[0])
            return max_file_id


disk_map = load_data("input.txt")
blocks = generate_blocks(disk_map)

max_file_id = get_max_file_id(blocks)
#  pprint(blocks)
for file_id in range(max_file_id, -1, -1):

    #  Progress-bar
    #  if file_id % 1000 == 0:
    #      print(file_id)

    moved = move_block_at_fileid(blocks, file_id)

    # if moved:
    #    pprint(blocks)

print(compute_checksum(blocks))
