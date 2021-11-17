# i know this and the past answer are pretty jank. there's def a more elegant way
# to solve for higher dimensions, rather than just copy pasting the 3dim solution.
# but eh im tired. dont want to overengineer right? also not sure if the
# defaultdict is really the way to go, this implementation takes 4.3s to complete.

from collections import defaultdict
from itertools import product

def addps(p1,p2):
    return (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2])

def getnextchar(idx,pocketdim):
    neighbors = set(addps(idx,n) for n in product([-1,0,1],[-1,0,1],[-1,0,1]))
    neighbors.remove(idx)
    count = sum([1 for n in neighbors if pocketdim[n] == '#'])
    if pocketdim[idx] == '#':
        if count == 2 or count == 3:
            return '#'
    else:
        if count == 3:
            return '#'
    return '.'

def update(pocketdim):
    mini = min((trip[0] for trip,val in pocketdim.items() if val=='#')) - 1
    maxi = max((trip[0] for trip,val in pocketdim.items() if val=='#')) + 2
    minj = min((trip[1] for trip,val in pocketdim.items() if val=='#')) - 1
    maxj = max((trip[1] for trip,val in pocketdim.items() if val=='#')) + 2
    mink = min((trip[2] for trip,val in pocketdim.items() if val=='#')) - 1
    maxk = max((trip[2] for trip,val in pocketdim.items() if val=='#')) + 2
    
    newdim = pocketdim.copy()
    for idx in product(range(mini,maxi),range(minj,maxj),range(mink,maxk)):
        newdim[idx] = getnextchar(idx,pocketdim)
    return newdim

def part1(file):
    with open(file) as f:
        pocketdim = defaultdict(lambda:'.')
        lines = f.readlines()
        for i,line in enumerate(lines):
            for j,ch in enumerate(line):
                if ch == '#':
                    pocketdim[(i,j,0)] = '#'
        for _ in range(6):
            pocketdim = update(pocketdim)
        print(sum([1 for key,val in pocketdim.items() if val == '#']))

#-------------------------------------------------------------------------------    
def addps2(p1,p2):
    return (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2],p1[3]+p2[3])

def getnextchar2(idx,pocketdim):
    neighbors = set(addps2(idx,n) for n in product([-1,0,1],[-1,0,1],[-1,0,1],[-1,0,1]))
    neighbors.remove(idx)
    count = sum([1 for n in neighbors if pocketdim[n] == '#'])
    if pocketdim[idx] == '#':
        if count == 2 or count == 3:
            return '#'
    else:
        if count == 3:
            return '#'
    return '.'

def update2(pocketdim):
    mini = min((trip[0] for trip,val in pocketdim.items() if val=='#')) - 1
    maxi = max((trip[0] for trip,val in pocketdim.items() if val=='#')) + 2
    minj = min((trip[1] for trip,val in pocketdim.items() if val=='#')) - 1
    maxj = max((trip[1] for trip,val in pocketdim.items() if val=='#')) + 2
    mink = min((trip[2] for trip,val in pocketdim.items() if val=='#')) - 1
    maxk = max((trip[2] for trip,val in pocketdim.items() if val=='#')) + 2
    minl = min((trip[3] for trip,val in pocketdim.items() if val=='#')) - 1
    maxl = max((trip[3] for trip,val in pocketdim.items() if val=='#')) + 2
    
    newdim = pocketdim.copy()
    for idx in product(range(mini,maxi),range(minj,maxj),range(mink,maxk),range(minl,maxl)):
        newdim[idx] = getnextchar2(idx,pocketdim)
    return newdim

def part2(file):
    with open(file) as f:
        pocketdim = defaultdict(lambda:'.')
        lines = f.readlines()
        for i,line in enumerate(lines):
            for j,ch in enumerate(line):
                if ch == '#':
                    pocketdim[(i,j,0,0)] = '#'
        for _ in range(6):
            pocketdim = update2(pocketdim)
        print(sum([1 for key,val in pocketdim.items() if val == '#']))
            

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()