from util.text import read_file_as_list

def p1():
    lines = read_file_as_list("input/day01/p1")
    location = 50
    zero_counter = 0
    for index, line in enumerate(lines):
        direction = line[0]
        amount = int(line[1:])
        if direction == "L":
            location = (location - amount) % 100
        elif direction == "R":
            location = (location + amount) % 100

        if location == 0:
            zero_counter += 1

    return zero_counter

def p2():
    lines = read_file_as_list("input/day01/p1")
    location = 50
    zero_counter = 0
    for index, line in enumerate(lines):
        direction = line[0]
        amount = int(line[1:])
        if direction == "L":
            if amount > location:
                if location == 0:
                    zero_counter -= 1
                zero_counter += amount // 100
                if location - (amount % 100) < 0:
                    zero_counter += 1
            location = (location - amount) % 100
        elif direction == "R":
            if location + amount > 100:
                zero_counter += amount // 100
                if location + (amount % 100) > 100:
                    zero_counter += 1
            location = (location + amount) % 100

        if location == 0:
            zero_counter += 1

    return zero_counter


if __name__ == "__main__":
    print(p1())
    print(p2())
