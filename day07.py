from dataclasses import dataclass
from enum import Enum

from util.text import read_file_as_list


class LmntType(Enum):
    START = 0
    SPLITTER = 1
    SPACE = 2
    BEAM = 3


class LmntStatus(Enum):
    COLD = 0
    HOT = 1


@dataclass
class Lmnt:
    lmnt_type: LmntType
    lmnt_status: LmntStatus
    beam_count: int

    def __init__(self, character: str) -> None:
        self.lmnt_status = LmntStatus.COLD
        self.char = character
        self.beam_count = 0
        match character:
            case "S":
                self.lmnt_type = LmntType.START
            case "^":
                self.lmnt_type = LmntType.SPLITTER
            case ".":
                self.lmnt_type = LmntType.SPACE

    def emit_beam(self) -> None:
        self.beam_count += 1
        self.lmnt_type = LmntType.BEAM

    def __str__(self) -> str:
        if self.lmnt_type == LmntType.BEAM:
            return str(self.beam_count)
        else:
            return self.char


def run_beam_splitter(lmnts: list[list[Lmnt]]) -> list[list[Lmnt]]:
    for y, row in enumerate(lmnts):
        for x, lmnt in enumerate(row):
            if y == 0 and lmnt.lmnt_type == LmntType.SPACE:
                continue
            if lmnt.lmnt_type == LmntType.START:
                lmnts[y + 1][x].lmnt_type = LmntType.BEAM
                lmnts[y + 1][x].beam_count = 1
                continue

            if lmnts[y - 1][x].lmnt_type == LmntType.BEAM:
                incoming_beam_count = lmnts[y - 1][x].beam_count
                if lmnt.lmnt_type == LmntType.SPLITTER:
                    lmnt.lmnt_status = LmntStatus.HOT
                    # Left
                    lmnts[y][x - 1].lmnt_type = LmntType.BEAM
                    lmnts[y][x - 1].beam_count += incoming_beam_count
                    # Right
                    lmnts[y][x + 1].lmnt_type = LmntType.BEAM
                    lmnts[y][x + 1].beam_count += incoming_beam_count
                else:
                    lmnt.lmnt_type = LmntType.BEAM
                    lmnt.beam_count += lmnts[y - 1][x].beam_count
    return lmnts


def get_hot_splitter_count(lmnts: list[list[Lmnt]]) -> int:
    count = 0
    for row in lmnts:
        for lmnt in row:
            if lmnt.lmnt_status == LmntStatus.HOT:
                count += 1
    return count


def display_path_count(lmnts: list[list[Lmnt]]) -> None:
    for y, row in enumerate(lmnts):
        if y % 2 != 0:
            print(f"Row {y:<3} =              :{''.join(str(lmnt) for lmnt in row)}")
            continue
        row_count = 0
        for x, lmnt in enumerate(row):
            if lmnt.lmnt_type == LmntType.BEAM:
                row_count += lmnt.beam_count
        print(f"Row {y:<3} = {row_count:<12} :{''.join(str(lmnt) for lmnt in row)}")


if __name__ == "__main__":
    schematic = read_file_as_list("input/day07/p1")
    lmnts = []
    for row in schematic:
        lmnts.append([Lmnt(x) for x in row])

    lmnts = run_beam_splitter(lmnts)
    print(f"Part 1: {get_hot_splitter_count(lmnts)}")
    # display_path_count(lmnts)
    print(f"Part 2: {sum(lmnt.beam_count for lmnt in lmnts[-1])}")
