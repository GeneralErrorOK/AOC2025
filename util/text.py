def read_file_as_list(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()
