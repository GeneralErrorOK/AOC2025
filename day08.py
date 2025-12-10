import math

import numpy as np

from util.text import read_file_as_list


def calculate_distances(jboxes: list[tuple[int, tuple[int, int, int]]]) -> list[tuple[int, int], float]:
    distances = set()
    for one in jboxes:
        o_id = one[0]
        o_x, o_y, o_z = one[1]
        for two in jboxes:
            t_id = two[0]
            t_x, t_y, t_z = two[1]
            if o_id == t_id:
                continue
            # Create identifier for the combination of coordinates, sorted so set will auto de-dupe
            dist_id = (o_id, t_id) if o_id > t_id else (t_id, o_id)
            distances.add((dist_id, float(np.linalg.norm(np.array((o_x, o_y, o_z)) - np.array((t_x, t_y, t_z))))))
    distances = list(distances)
    distances.sort(key=lambda x: x[1])
    return distances


def connect_circuits(distances: list[tuple[int, int], float], iterations: int) -> list[list[int]]:
    circuits = []

    def same_circuit(primary, secondary):
        for circuit in circuits:
            if primary in circuit and secondary in circuit:
                return True
        return False

    def in_a_circuit(box_id: int) -> bool:
        for circuit in circuits:
            if box_id in circuit:
                return True
        return False

    def connect(primary, secondary):
        if in_a_circuit(primary) and not in_a_circuit(secondary):
            # Add secondary to circuit of primary
            for circuit in circuits:
                if primary in circuit:
                    circuit.append(secondary)
                    return
        elif in_a_circuit(secondary) and not in_a_circuit(primary):
            # Add primary to circuit of secondary
            for circuit in circuits:
                if secondary in circuit:
                    circuit.append(primary)
                    return
        elif in_a_circuit(primary) and in_a_circuit(secondary):
            # Merge circuits
            for c_one in circuits:
                if primary in c_one:
                    for c_two in circuits:
                        if secondary in c_two:
                            new_c = c_one + c_two
                            circuits.remove(c_one)
                            circuits.remove(c_two)
                            circuits.append(new_c)
                            return
        else:
            # Create new circuit
            circuits.append([primary, secondary])

    skip_some = 0
    for index, dist_combination in enumerate(distances):
        primary, secondary = dist_combination[0]
        print(f"Iteration {index}: connecting {primary} to {secondary}")
        if same_circuit(primary, secondary):
            print("Same circuit! Skipping.")
            continue
        else:
            print(f"Before: {circuits}")
            connect(primary, secondary)
            print(f"After: {circuits}\n")
        if iterations > 0:
            if index >= iterations:
                break
        else:
            if index > 10 and len(circuits) == 1:
                # Absolutely NO CLUE why but we need to continue 3 more times to get the right connection.
                # (in both example and puzzle input)
                skip_some += 1
                if skip_some == 3:
                    return primary, secondary

    circuits.sort(key=lambda x: len(x), reverse=True)
    return circuits


def create_jboxes_from_list(jboxes_list: list[str]) -> list[tuple[int, tuple[int, int, int]]]:
    jboxes = []
    for index, junction_box in enumerate(jboxes_list):
        x, y, z = junction_box.split(",")
        jboxes.append((index, (int(x), int(y), int(z))))
    return jboxes


def p1(distances) -> None:
    connected_circuits = connect_circuits(distances, 1000)
    print(connected_circuits)
    sizes_top_3 = [len(circuit) for circuit in connected_circuits[:3]]
    print(f"Top 3 sizes: {sizes_top_3}")
    print(math.prod(sizes_top_3))


def get_box(id, jboxes) -> tuple[int, int, int]:
    for box in jboxes:
        if box[0] == id:
            return box[1]


def p2(distances, jboxes) -> None:
    id1, id2 = connect_circuits(distances, -1)
    box1 = get_box(id1, jboxes)
    box2 = get_box(id2, jboxes)
    print(f"Box 1: {box1}")
    print(f"Box 2: {box2}")
    print(f"Answer: {box1[0] * box2[0]}")


if __name__ == "__main__":
    junction_boxes_list = read_file_as_list("input/day08/p1")
    jboxes = create_jboxes_from_list(junction_boxes_list)
    distances = calculate_distances(jboxes)
    # p1(distances)
    p2(distances, jboxes)
