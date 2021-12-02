

def part1(file):
    with open(file) as f:
        directions = [l.split() for l in f.readlines()]
        directions = [(d[0],int(d[1])) for d in directions]
    hpos = 0
    vpos = 0
    for d in directions:
        match d[0]:
            case 'forward': hpos += d[1]
            case 'up':      vpos -= d[1]
            case 'down':    vpos += d[1]
    print(hpos*vpos)

#-------------------------------------------------------------------------------

def part2(file):
    with open(file) as f:
        directions = [l.split() for l in f.readlines()]
        directions = [(d[0],int(d[1])) for d in directions]
    aim = 0
    hpos = 0
    vpos = 0
    for d in directions:
        match d[0]:
            case 'up':   aim -= d[1]
            case 'down': aim += d[1]
            case 'forward':
                hpos += d[1]
                vpos += aim * d[1]
    print(hpos*vpos)

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()