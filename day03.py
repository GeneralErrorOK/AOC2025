from util.text import read_file_as_list


def get_best_combination(bank: str) -> str:
    h1 = 0
    i1 = 0
    for index, jolt_rating in enumerate(bank):
        if index == len(bank) - 1:
            break
        if int(jolt_rating) > h1:
            h1 = int(jolt_rating)
            i1 = index
    h2 = 0
    for index, jolt_rating in enumerate(bank[i1 + 1 :]):
        if int(jolt_rating) > h2:
            h2 = int(jolt_rating)

    return f"{h1}{h2}"


def get_highest_jolt_rating(bank: str, length: int, combination: str = "") -> str:
    if length == 0:
        return combination

    if length == len(bank):
        return combination + bank

    if length == 1:
        clipped_bank = bank
    else:
        clipped_bank = bank[: -length + 1]

    highest = 0
    index = 0
    for i, num in enumerate(clipped_bank):
        if int(num) > highest:
            highest = int(num)
            index = i

    combination += str(highest)

    return get_highest_jolt_rating(bank[index + 1 :], length - 1, combination)


def p1():
    bat_banks = read_file_as_list("input/day03/p1")
    sum_voltage = 0
    for bank in bat_banks:
        best_combination = get_best_combination(bank)
        print(f"{bank}: {best_combination}")
        sum_voltage += int(best_combination)

    return sum_voltage


def p2():
    bat_banks = read_file_as_list("input/day03/p1")
    sum_voltage = 0
    for bank in bat_banks:
        best_combination = get_highest_jolt_rating(bank, 12)
        print(f"{bank}: {best_combination}")
        sum_voltage += int(best_combination)

    return sum_voltage


if __name__ == "__main__":
    print(p2())
