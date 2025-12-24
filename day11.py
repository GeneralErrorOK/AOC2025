
from util.text import read_file_as_list


def path_count(devices: dict, node: str, exits=[], target = None) -> list[int]:
    output = devices.get(node)
    if target is None:
        target = "out"

    if output[0] == target:
        print(f"{node}: exit")
        exits.append(1)
        return exits
    print(f"{node}: {len(output)} paths ({output})")

    for device in output:
        exits = path_count(devices, device, exits)
        print(f"{device}: {exits}")

    return exits

def p1() -> int:
    device_list = read_file_as_list("input/day11/p1")
    devices = {}
    for device_row in device_list:
        device, outputs = device_row.split(":")
        devices[device] = outputs.split()

    exits = path_count(devices, "you")

    return sum(exits)

def p2() -> int:
    device_list = read_file_as_list("input/day11/ex2")
    devices = {}
    for device_row in device_list:
        device, outputs = device_row.split(":")
        devices[device] = outputs.split()

    svr_dac = path_count(devices, "svr", target="dac")
    dac_fft = path_count(devices, "dac", target="fft")
    fft_out = path_count(devices, "fft", target="out")

    return sum(svr_dac) + sum(dac_fft) + sum(fft_out)

if __name__ == "__main__":
    print(p2())
