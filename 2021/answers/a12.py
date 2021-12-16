# woof what can i say except damn this puzzle was freaking hard for me. my solution
# also ends up taking like 10 seconds to run, so I'm sure there has to be a better
# method. oh well i got the star on the website and that's really what the spirit
# of christmas is all about. 

from copy import deepcopy

def getpaths(start,stop,caves):
    if start == stop:
        return [[start]]
    paths = []
    for child in caves[stop]:
        if caves[child][stop]:
            ccopy = deepcopy(caves)
            if stop.islower():
                for ic in ccopy:
                    if stop in ccopy[ic]:
                        ccopy[ic][stop] = False
            paths += [np + [stop] for np in getpaths(start,child,ccopy)]    
    return paths
    
def part1(file):
    with open(file) as f:
        lines = [l.strip().split('-') for l in f.readlines()]
        caves = {}
        for l in lines:
            if l[0] not in caves:
                caves[l[0]] = {}
            if l[1] not in caves:
                caves[l[1]] = {}
            caves[l[0]][l[1]] = True
            caves[l[1]][l[0]] = True

        print(len(getpaths('start','end',caves)))

#-------------------------------------------------------------------------------

def getpaths2(start,stop,caves,visits,lower):
    if start == stop:
        return [[start]]
    paths = []
    for child in caves[stop]:
        if visits[child] > 0:
            if stop.islower():
                if visits[stop] == 2:
                    v1 = deepcopy(visits)
                    v2 = deepcopy(visits)

                    v1[stop] -= 1
                    for l in lower:
                        if v1[l] == 2:
                            v1[l] -= 1

                    v2[stop] = 0

                    p1 = set(tuple(np + [stop]) for np in getpaths2(start,child,caves,v1,lower))
                    p2 = set(tuple(np + [stop]) for np in getpaths2(start,child,caves,v2,lower))
                    paths += [list(pth) for pth in p1.union(p2)]
                else:
                    v1 = deepcopy(visits)
                    v1[stop] -= 1
                    paths += [np + [stop] for np in getpaths2(start,child,caves,v1,lower)]
            else:
                v1 = deepcopy(visits)
                paths += [np + [stop] for np in getpaths2(start,child,caves,v1,lower)]

    return paths

def part2(file):
    with open(file) as f:
        lines = [l.strip().split('-') for l in f.readlines()]
        caves = {}
        for l in lines:
            if l[0] not in caves:
                caves[l[0]] = {}
            if l[1] not in caves:
                caves[l[1]] = {}
            caves[l[0]][l[1]] = True
            caves[l[1]][l[0]] = True

        visited = {k:2 for k in caves}
        visited['start'] = 1
        visited['end'] = 1
        lower = [l for l in caves if (l.islower() and l != 'end' and l != 'start')]

        print(len(getpaths2('start','end',caves,visited,lower)))

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()