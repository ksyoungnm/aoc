import numpy as np

def getneighbors(p,mind,maxd):
    neighbs = set()
    neighbs.add((p[0]-1,p[1]-1))
    neighbs.add((p[0]  ,p[1]-1))
    neighbs.add((p[0]+1,p[1]-1))
    neighbs.add((p[0]-1,p[1]  ))
    neighbs.add((p[0]+1,p[1]  ))
    neighbs.add((p[0]-1,p[1]+1))
    neighbs.add((p[0]  ,p[1]+1))
    neighbs.add((p[0]+1,p[1]+1))
    neighbs = [n for n in neighbs if (mind <= n[0] < maxd) and (mind <= n[1] < maxd) ]
    for n in neighbs:
        yield n

def part1(file):
    octos = np.genfromtxt(file, dtype=int, delimiter=1)
    steps = 100
    count = 0
    for _ in range(steps):
        octos += 1
        flashes = set(zip(*np.where(octos>9)))
        done = set()
        while len(flashes) > 0:
            p = flashes.pop()
            for pp in getneighbors(p,0,len(octos)):
                octos[pp] += 1
                if octos[pp] > 9 and pp not in done:
                    flashes.add(pp)
            done.add(p)

        for p in done:
            octos[p] = 0

        count += len(done)
    print(count)


#-------------------------------------------------------------------------------

def part2(file):
    octos = np.genfromtxt(file, dtype=int, delimiter=1)
    step = 0
    while not np.all(octos == 0):
        octos += 1
        flashes = set(zip(*np.where(octos>9)))
        done = set()
        while len(flashes) > 0:
            p = flashes.pop()
            for pp in getneighbors(p,0,len(octos)):
                octos[pp] += 1
                if octos[pp] > 9 and pp not in done:
                    flashes.add(pp)
            done.add(p)

        for p in done:
            octos[p] = 0
        step += 1

    print(step)

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()