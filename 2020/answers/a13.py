
def part1(file):
    with open(file) as f:
        target,buses = f.readlines()
        target = int(target)
        buses = [int(ch) for ch in buses.split(',') if ch!='x']
        nextavail = [(int(target/bus)+1)*bus for bus in buses]
        imin = min(range(len(nextavail)),key=nextavail.__getitem__)
        print(buses[imin]*(nextavail[imin]-target))

def getiter(offset,cycle,prime,target):
    while True:
        if offset % prime == target:
            return (offset, cycle*prime)
        offset += cycle

def part2(file):
    with open(file) as f:
        _,buses = f.readlines()
        buses = [bus.strip() for bus in buses.split(',')]
        remainders = [i for i in range(len(buses)) if buses[i] != 'x']
        buses = [int(buses[i]) for i in remainders]
        remainders = [(-rem)%buses[i] for i,rem in enumerate(remainders)]

        offset = 0
        cycle = 1
        for bus,rem in zip(buses,remainders):
            offset,cycle = getiter(offset,cycle,bus,rem)
        print(offset)


def main():
    filename = '../example.txt'
    filename = '../datasets/13.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
