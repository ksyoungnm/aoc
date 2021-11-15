
def part1(file):
    with open(file) as f:
        # splits up each relevant piece of info
        pwrds = [l.split() for l in f.readlines()]
        # change min/max into a tuple of ints
        pwrds = [[tuple(map(int,p[0].split('-'))),p[1],p[2]] for p in pwrds]
        # get rid of colon in the second field
        pwrds = [[p[0],p[1].replace(':',''),p[2]] for p in pwrds]

        valid = 0
        for p in pwrds:
            occur = p[2].count(p[1])
            if occur >= p[0][0] and occur <= p[0][1]:
                valid += 1

        print(valid)

def part2(file):
    with open(file) as f:
        # as above
        pwrds = [l.split() for l in f.readlines()]
        pwrds = [[tuple(map(int,p[0].split('-'))),p[1],p[2]] for p in pwrds]
        pwrds = [[p[0],p[1].replace(':',''),p[2]] for p in pwrds]

        valid = 0
        for p in pwrds:
            ch1 = p[2][p[0][0]-1] == p[1]
            ch2 = p[2][p[0][1]-1] == p[1]
            if ch1 != ch2:
                valid += 1

        print(valid)

def main():
    # filename = '../example.txt'
    filename = '../datasets/2.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
