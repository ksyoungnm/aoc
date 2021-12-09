from itertools import product

def getlows(floor):
    lows = []
    for i,j in product(range(len(floor)),range(len(floor[0]))):
        if i > 0 and floor[i-1][j] <= floor[i][j]: continue
        if i < len(floor)-1 and floor[i+1][j] <= floor[i][j]: continue
        if j > 0 and floor[i][j-1] <= floor[i][j]: continue
        if j < len(floor[0])-1 and floor[i][j+1] <= floor[i][j]: continue
        lows.append((i,j))
    return lows

def part1(file):
    with open(file) as f:
        floor = [list(map(int,l.strip())) for l in f.readlines()]
        lows = getlows(floor)
        total = 0
        for p in lows:
            total += floor[p[0]][p[1]] + 1
        print(total)

#-------------------------------------------------------------------------------

def findcloselow(p, lows, floor):
    if floor[p[0]][p[1]] == 9:
        return None
    while p not in lows:
        checks = set()
        if p[0] > 0: checks.add((p[0]-1,p[1]))
        if p[1] > 0: checks.add((p[0],p[1]-1))
        if p[0] < len(floor)-1: checks.add((p[0]+1,p[1]))
        if p[1] < len(floor[0])-1: checks.add((p[0],p[1]+1))

        checks = [c for c in checks if floor[c[0]][c[1]] != 9]
        p = min(checks, key=lambda x:floor[x[0]][x[1]])
    return p

def part2(file):
    with open(file) as f:
        floor = [list(map(int,l.strip())) for l in f.readlines()]
        lows = [l for l in getlows(floor)]
        lowd = {l:0 for l in lows}

        for i,j in product(range(len(floor)),range(len(floor[0]))):
            closelow = findcloselow((i,j), lows, floor)
            if closelow is not None:
                lowd[closelow] += 1

        bigbs = list(sorted(lowd.values(),reverse=True))

        print(bigbs[0]*bigbs[1]*bigbs[2])

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()