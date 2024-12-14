

import os
import re



def part1(filename):

    with open(filename) as f:
        line = f.read()
        pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
        total = 0
        for mul in pattern.findall(line):
            mul = [int(x) for x in mul.strip("mul(").strip(")").split(",")]
            total += mul[0] * mul[1]
        print(total)
            # print(mul[0] * mul[1])
        # print(*pattern.findall(line), sep = '\n')



def part2(filename):
    with open(filename) as f:
        line = f.read()
        pattern = re.compile(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)")
        enabled = True
        total = 0
        for mul in pattern.findall(line):
            if mul == "do()":
                enabled = True
            elif mul == "don't()":
                enabled = False
            else:
                if enabled:
                    mul = [int(x) for x in mul.strip("mul(").strip(")").split(",")]
                    total += mul[0] * mul[1]

        print(total)



def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
