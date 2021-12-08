# wow this puzzle was great haha. i decided to go the analytical route, and i
# think i can prove (w/ derivatives) that the optimal center for the first part
# has to be the median, and (this was harder) the optimal center for the second
# has to be within +or- 1 of the mean. there might be a way to determine if its
# the floor or the ceiling based on the proportion of values on either side of
# mean, but i thought for now just having to check the two values is good enough

import numpy as np

def part1(file):
    crabs = np.loadtxt(file, dtype=int, delimiter=',')
    med = int(np.median(crabs))
    print(sum(abs(crabs - med)))

#-------------------------------------------------------------------------------

def part2(file):
    crabs = np.loadtxt(file, dtype=int, delimiter=',')
    mean = np.mean(crabs)
    mfloor,mceil = int(np.floor(mean)), int(np.ceil(mean))
    fuel = lambda agg: sum(abs(crabs - agg) * (abs(crabs - agg)+1)) // 2
    print(min(fuel(mfloor),fuel(mceil)))

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()