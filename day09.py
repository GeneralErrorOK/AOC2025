from shapely import LineString, Polygon, Point

from util.text import read_file_as_list


def p1() -> int:
    tile_coords = read_file_as_list("input/day09/p1")
    tiles = []
    for tile in tile_coords:
        x, y = tile.split(",")
        tiles.append((int(x), int(y)))

    squares = []
    for t1 in tiles:
        for t2 in tiles:
            if t1 is t2:
                continue
            x1, y1 = t1
            x2, y2 = t2

            if x1 < x2:
                x_dim = x2 - x1
            else:
                x_dim = x1 - x2

            if y1 < y2:
                y_dim = y2 - y1
            else:
                y_dim = y1 - y2
            x_dim += 1
            y_dim += 1
            squares.append(x_dim * y_dim)

    squares.sort()
    return squares[-1]

def filter_tiles(tiles: list[tuple[int, int]], line_segments: list[Point]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    super_polygon = Polygon(line_segments)
    squares_that_fit = []
    for t1 in tiles:
        for t2 in tiles:
            if t1 is t2:
                continue
            x1, y1 = t1
            x2, y2 = t2
            square = Polygon(((x1, y1), (x2, y1), (x2, y2), (x1, y2)))
            if super_polygon.contains(square):
                # Now we have to grow the polygon by 1 in x and y dimensions for area to work as expected?
                poly = Polygon(((x1 - 1, y1 - 1), (x2 + 1, y1 - 1), (x2 + 1, y2 + 1), (x1 - 1, y2 + 1)))
                squares_that_fit.append(poly)
    return squares_that_fit


def p2() -> int:
    tile_coords = read_file_as_list("input/day09/p1")
    tiles = []
    for tile in tile_coords:
        x, y = tile.split(",")
        tiles.append((int(x), int(y)))

    points = [Point(x, y) for x, y in tiles]
    fit: list[Polygon] = filter_tiles(tiles, points)
    dimensions = [sq.area for sq in fit]
    dimensions.sort()
    return dimensions[-1]




if __name__ == "__main__":
    print(p2())
