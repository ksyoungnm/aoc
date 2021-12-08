from collections import defaultdict, Counter

def lineiter(p1,p2):
    s1 = (p2[0]-p1[0]) // abs(p2[0]-p1[0]) if (p2[0]-p1[0]) != 0 else 0
    s2 = (p2[1]-p1[1]) // abs(p2[1]-p1[1]) if (p2[1]-p1[1]) != 0 else 0
    yield p1
    while p1 != p2:
        p1 = (p1[0]+s1,p1[1]+s2)
        yield p1

def part1(file):
    with open(file) as f:

        lines = [l.strip().split(' -> ') for l in f.readlines()]
        lines = [(tuple(map(int,l[0].split(','))),tuple(map(int,l[1].split(',')))) for l in lines]
        # filter for only straight line seggies
        lines = [l for l in lines if (l[0][0] == l[1][0] or l[0][1] == l[1][1])]

        spots = defaultdict(int)
        for line in lines:
            for p in lineiter(*line):
                spots[p] += 1
        
        print(sum(1 for sp in spots.values() if sp >= 2))
        
#-------------------------------------------------------------------------------

def part2(file):
    with open(file) as f:
        
        lines = [l.strip().split(' -> ') for l in f.readlines()]
        lines = [(tuple(map(int,l[0].split(','))),tuple(map(int,l[1].split(',')))) for l in lines]

        spots = defaultdict(int)
        for line in lines:
            for p in lineiter(*line):
                spots[p] += 1

        print(sum(1 for sp in spots.values() if sp >= 2))

def dontlook(file):
    print(sum(1 for val in Counter(p for line in [(tuple(map(int,l[0].split(','))),tuple(map(int,l[1].split(',')))) for l in [l.split(' -> ') for l in open(file)]] for p in lineiter(*line)).values() if val >= 2))
        
#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = '../datasets/5.txt'
    part1(filename)
    part2(filename)
    dontlook(filename)

if __name__ == '__main__':
    main()