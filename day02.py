from util.text import read_file_as_list

def is_mirrored_id(product_id: str) -> bool:
    # Can't be repeating if it's odd
    if len(product_id) % 2 != 0:
        return False

    mid = int(len(product_id) // 2)
    left_side = product_id[:mid]
    right_side = product_id[mid:]
    return left_side == right_side

def is_repeating_id(product_id: str, pattern_length: int = 1) -> bool:
    id_length = len(product_id)
    # We've reached more than half, can't repeat. Base case
    if pattern_length > id_length // 2:
        return False

    # This pattern length can't repeat in current length, recurse
    if id_length % pattern_length != 0:
        return is_repeating_id(product_id, pattern_length + 1)

    pattern = product_id[:pattern_length]
    for i in range(0, id_length, pattern_length):
        if product_id[i:i + pattern_length] != pattern:
            return is_repeating_id(product_id, pattern_length + 1)

    return True

def p1():
    ids = read_file_as_list("input/day02/p1")
    id_ranges = ids[0].split(",")
    counter = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        for product_id in range(int(start), int(end) + 1):
            if is_mirrored_id(str(product_id)):
                counter += product_id
    return counter

def p2():
    ids = read_file_as_list("input/day02/p1")
    id_ranges = ids[0].split(",")
    counter = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        for product_id in range(int(start), int(end) + 1):
            if is_repeating_id(str(product_id)):
                print(product_id)
                counter += product_id
    return counter

if __name__ == "__main__":
    print(p2())
