


def part1(file):
    with open(file) as f:
        depths = [int(l) for l in f.readlines()]
        count = 0
        previous = depths[0]
        for depth in depths[1:]:
            if depth > previous:
                count += 1
            previous = depth
        print(count)

#-------------------------------------------------------------------------------

def part2(file):
    with open(file) as f:
        depths = [int(l) for l in f.readlines()]
        count = 0
        previous = sum(depths[:3])
        for i in range(1,len(depths)-2):
            depth = sum(depths[i:i+3])
            if depth > previous:
                count += 1
            previous = depth
        print(count)

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()