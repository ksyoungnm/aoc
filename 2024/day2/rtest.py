

from itertools import pairwise

import os

def check_line(line):
    diffs = [a - b for (a,b) in pairwise(line)]
    if (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        if all(abs(d) < 4 for d in diffs):
            return True
    return False

def check_line_dampened(line):
    if check_line(line):
        return True

    for i in range(len(line)):
        if check_line(line[:i] + line[i+1:]):
            return True

    return False


def part1(filename):

    with open(filename) as f:
        lines =[[int(x) for x in l.strip().split()] for l in f.readlines()]
        total = 0
        for line in lines:
            if check_line(line):
                total += 1
        print(total)


def part2(filename):
    with open(filename) as f:
        lines =[[int(x) for x in l.strip().split()] for l in f.readlines()]
        total = 0
        for line in lines:
            if check_line_dampened(line):
                total += 1
        print(total)

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
