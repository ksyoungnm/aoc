
import os
import itertools

def calc_val(equat, ops):
    assert len(ops) == len(equat) - 1
    val = equat[0]
    for i,op in enumerate(ops):
        if op == "+":
            val += equat[i+1]
        elif op == "||":
            val = int(str(val) + str(equat[i+1]))
        else:
            val *= equat[i+1]
    return val

def can_make(result, equat):
    for ops in itertools.product(["+", "*"], repeat=len(equat)-1):
        if calc_val(equat, ops) == result:
            return True
    return False

def can_make_2(result, equat):
    for ops in itertools.product(["+", "*", "||"], repeat=len(equat)-1):
        if calc_val(equat, ops) == result:
            return True
    return False

def part1(filename):

    with open(filename) as f:
        lines = [tuple(l.strip().split(': ')) for l in f.readlines()]
        results = [int(x[0]) for x in lines]
        equations = [[int(y) for y in x[1].split()] for x in lines]

        total = 0
        for result, equat in zip(results, equations):
            if can_make(result, equat):
                total +=  result
        print(total)


def part2(filename):

    with open(filename) as f:
        lines = [tuple(l.strip().split(': ')) for l in f.readlines()]
        results = [int(x[0]) for x in lines]
        equations = [[int(y) for y in x[1].split()] for x in lines]

        total = 0
        for result, equat in zip(results, equations):
            if can_make_2(result, equat):
                total +=  result
        print(total)

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
