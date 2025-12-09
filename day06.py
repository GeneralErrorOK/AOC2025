import math

from util.text import read_file_as_list


def p1():
    math_challenges = read_file_as_list("input/day06/p1")
    first = math_challenges[0].split()
    second = math_challenges[1].split()
    third = math_challenges[2].split()
    fourth = math_challenges[3].split()
    operations = math_challenges[4].split()
    grand_total = 0

    for i, operation in enumerate(operations):
        if operation == "*":
            grand_total += int(first[i]) * int(second[i]) * int(third[i]) * int(fourth[i])
        if operation == "+":
            grand_total += int(first[i]) + int(second[i]) + int(third[i]) + int(fourth[i])

    return grand_total


def p2():
    math_challenges = read_file_as_list("input/day06/p1")
    row_one = math_challenges[0]
    row_two = math_challenges[1]
    row_three = math_challenges[2]
    row_four = math_challenges[3]
    operations = math_challenges[4]

    grand_total = 0
    numbers = []
    for i in range(len(row_one) - 1, -1, -1):
        numbers.append(row_one[i] + row_two[i] + row_three[i] + row_four[i])

        if operations[i] != " ":
            cleaned = [number.strip() for number in numbers]
            stage = [int(number) for number in cleaned if number.isdigit()]
            if operations[i] == "+":
                grand_total += sum(stage)
                print(f"{i} +: {stage}")
            elif operations[i] == "*":
                print(f"{i} *: {stage}")
                grand_total += math.prod(stage)
            numbers = []

    return grand_total


if __name__ == "__main__":
    print(p2())
