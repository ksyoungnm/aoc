import os
import itertools


def count_antinodes(grid):
    bounds_i = len(grid)
    bounds_j = len(grid[0])
    total_antinodes = set()

    ch_freqs = dict()
    for ch_i, gridline in enumerate(grid):
        for ch_j in range(len(gridline)):
            ch = grid[ch_i][ch_j]
            if ch != ".":
                if ch in ch_freqs:
                    ch_freqs[ch].append((ch_i, ch_j))
                else:
                    ch_freqs[ch] = [(ch_i, ch_j)]

    for ch in ch_freqs:
        for p1,p2 in itertools.permutations(ch_freqs[ch], 2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            test_point = (p2[0] + dx, p2[1] + dy)
            test_bounds_x = 0 <= test_point[0] < bounds_i
            test_bounds_y = 0 <= test_point[1] < bounds_j

            if test_bounds_x and test_bounds_y:
                total_antinodes.add(test_point)

    return len(total_antinodes)

def in_bounds(point, bounds_i, bounds_j):
    test_bounds_x = 0 <= point[0] < bounds_i
    test_bounds_y = 0 <= point[1] < bounds_j
    return test_bounds_x and test_bounds_y

def count_antinodes_2(grid):
    bounds_i = len(grid)
    bounds_j = len(grid[0])
    total_antinodes = set()

    ch_freqs = dict()
    for ch_i, gridline in enumerate(grid):
        for ch_j in range(len(gridline)):
            ch = grid[ch_i][ch_j]
            if ch != ".":
                if ch in ch_freqs:
                    ch_freqs[ch].append((ch_i, ch_j))
                else:
                    ch_freqs[ch] = [(ch_i, ch_j)]

    for ch in ch_freqs:
        for p1,p2 in itertools.permutations(ch_freqs[ch], 2):
            # print(p1,p2,": ", end = "")
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            test_point = (p2[0], p2[1])
            while in_bounds(test_point, bounds_i, bounds_j):
                # print(test_point, end = "")
                total_antinodes.add(test_point)
                test_point = (test_point[0] + dx, test_point[1] + dy)
            # print()


    return len(total_antinodes)


def part1(filename):

    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
        print(count_antinodes(grid))


def part2(filename):

    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
        print(count_antinodes_2(grid))

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
