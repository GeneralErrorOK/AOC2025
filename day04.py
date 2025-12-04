from util.text import read_file_as_list


def position_occupied(rows: list[str], x: int, y: int) -> int:
    if x < 0 or x >= len(rows[0]) or y < 0 or y >= len(rows):
        return 0
    else:
        return 1 if rows[y][x] == "@" else 0


def count_accessible_rolls(rows: list[str]) -> tuple[int, list[str]]:
    accessible_rolls = 0
    new_rows = rows.copy()
    for y, row in enumerate(rows):
        for x, entry in enumerate(row):
            if entry == "@":
                count = 0
                # Top row
                count += position_occupied(rows, x - 1, y - 1)
                count += position_occupied(rows, x, y - 1)
                count += position_occupied(rows, x + 1, y - 1)

                # Neighbors
                count += position_occupied(rows, x - 1, y)
                count += position_occupied(rows, x + 1, y)

                # Bottom row
                count += position_occupied(rows, x - 1, y + 1)
                count += position_occupied(rows, x, y + 1)
                count += position_occupied(rows, x + 1, y + 1)

                if count < 4:
                    accessible_rolls += 1
                    new_rows[y] = new_rows[y][:x] + "." + new_rows[y][x + 1 :]

    return accessible_rolls, new_rows


def p1():
    rows = read_file_as_list("input/day04/p1")
    count, _ = count_accessible_rolls(rows)
    return count


def p2():
    rows = read_file_as_list("input/day04/p1")
    accessible_rolls = 0
    while True:
        count, rows = count_accessible_rolls(rows)
        if count == 0:
            break
        else:
            accessible_rolls += count

    return accessible_rolls


if __name__ == "__main__":
    print(p2())
