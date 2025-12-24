from util.text import read_file_as_list


def p1() -> int:
    machine_list = read_file_as_list("input/day10/p1")
    grand_total = 0
    for machine in machine_list:
        lights, *buttons, _ = machine.split()
        target_lights = sum(1 << i for i, char in enumerate(lights[1:-1]) if char == "#")
        btn_presses = [sum(1 << int(num) for num in btn[1:-1].split(",")) for btn in buttons]
        blinken_lights = {0}
        for i in range(1, 10_000_000):
            blinken_lights = set(lights ^ btn for lights in blinken_lights for btn in btn_presses)
            if target_lights in blinken_lights:
                grand_total += i
                break
    return grand_total


if __name__ == "__main__":
    print(p1())
