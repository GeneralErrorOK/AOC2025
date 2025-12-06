from util.text import read_file_as_list


def get_produce_data(rows: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    fresh_id_ranges = []
    stock_ids = []
    for row in rows:
        if "-" in row:
            id_range = row.split("-")
            # I'd rather unwrap all ranges into a set but that eats up gigabytes of memory...
            fresh_id_ranges.append((int(id_range[0]), int(id_range[1])))
        elif row != "":
            stock_ids.append(int(row))

    return fresh_id_ranges, stock_ids


def merge_ranges(ranges: list[list[int]]) -> list[list[int]]:
    # Sort the intervals based on the starting points
    ranges.sort(key=lambda x: x[0])

    merged_ranges = [ranges[0]]

    for current in ranges[1:]:
        last_merged = merged_ranges[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged_ranges.append(current)
    return merged_ranges


def p1():
    rows = read_file_as_list("input/day05/p1")
    fresh_id_ranges, stock_ids = get_produce_data(rows)
    fresh_produce = []
    for stock_id in stock_ids:
        for range in fresh_id_ranges:
            if range[0] <= stock_id <= range[1]:
                fresh_produce.append(stock_id)
                break

    return len(fresh_produce)


def p2():
    rows = read_file_as_list("input/day05/p1")
    fresh_id_ranges, _ = get_produce_data(rows)
    merged_ranges = merge_ranges([[a, b] for a, b in fresh_id_ranges])
    product_ids = sum((r[1] - r[0]) + 1 for r in merged_ranges)

    return product_ids


if __name__ == "__main__":
    print(p2())
