
def part1(file):
    with open(file) as f:
        nums = [int(l) for l in f.readlines()]

    for numi in nums:
        for numj in nums:
            if numi + numj == 2020:
                print(numi*numj)
                return

def part2(file):
    with open(file) as f:
        nums = [int(l) for l in f.readlines()]

    for numi in nums:
        for numj in nums:
            for numk in nums:
                if numi + numj + numk == 2020:
                    print(numi*numj*numk)
                    return

def main():
    filename = '../datasets/1.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
