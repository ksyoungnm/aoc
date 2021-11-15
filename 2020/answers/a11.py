import numpy as np
import itertools

def getcoords_pt1(i,j,ibs,jbs,chart):
    coords = set()
    coords.add((max(i-1,ibs[0]),max(j-1,jbs[0])))
    coords.add((max(i-1,ibs[0]),j))
    coords.add((max(i-1,ibs[0]),min(j+1,jbs[1])))
    coords.add((i,max(j-1,jbs[0])))
    coords.add((i,min(j+1,jbs[1])))
    coords.add((min(i+1,ibs[1]),max(j-1,jbs[0])))
    coords.add((min(i+1,ibs[1]),j))
    coords.add((min(i+1,ibs[1]),min(j+1,jbs[1])))
    return(coords-{(i,j)})

def findnextseat(i,j,ibs,jbs,di,chart):
    coord = (i,j)
    while True:
        coord = (coord[0]+di[0],coord[1]+di[1])
        if (coord[0] < ibs[0] or coord[0] > ibs[1] or coord[1] < jbs[0] or coord[1] > jbs[1]):
            return((i,j))
        if chart[coord] != '.':
            return coord

def getcoords_pt2(i,j,ibs,jbs,chart):
    coords = set()
    coords.add(findnextseat(i,j,ibs,jbs,(-1,-1),chart))
    coords.add(findnextseat(i,j,ibs,jbs,(-1,0),chart))
    coords.add(findnextseat(i,j,ibs,jbs,(-1,1),chart))
    coords.add(findnextseat(i,j,ibs,jbs,(0,-1),chart))
    coords.add(findnextseat(i,j,ibs,jbs,(0,1),chart))
    coords.add(findnextseat(i,j,ibs,jbs,(1,-1),chart))
    coords.add(findnextseat(i,j,ibs,jbs,(1,0),chart))
    coords.add(findnextseat(i,j,ibs,jbs,(1,1),chart))
    return(coords-{(i,j)})

def update(chart,part=1):
    if part == 1:
        crowd = 4
        getcoords = getcoords_pt1
    else: # part == 2
        crowd = 5
        getcoords = getcoords_pt2

    maxi,maxj = chart.shape
    newchart = chart.copy()
    for i,j in itertools.product(range(maxi),range(maxj)):
        if chart[i,j] == '.':
            continue
        coords_to_check = getcoords(i,j,(0,maxi-1),(0,maxj-1),chart)
        if chart[i,j] == 'L':
            unoccupied = len([1 for coord in coords_to_check if chart[coord] != '#'])
            if unoccupied == len(coords_to_check):
                newchart[i,j] = '#'
        if chart[i,j] == '#':
            occupied = len([1 for coord in coords_to_check if chart[coord] == '#'])
            if occupied >= crowd:
                newchart[i,j] = 'L'
    return newchart

def part1(file):
    with open(file) as f:
        previous = np.array([list(l.strip()) for l in f.readlines()],dtype=str)
        current = update(previous,part=1)
        while not (previous == current).all():
            previous = current
            current = update(current,part=1)
        print(np.sum(np.full_like(current,'#') == current))

def part2(file):
    with open(file) as f:
        previous = np.array([list(l.strip()) for l in f.readlines()],dtype=str)
        current = update(previous,part=2)
        while not (previous == current).all():
            previous = current
            current = update(current,part=2)
        print(np.sum(np.full_like(current,'#') == current))


def main():
    filename = '../example.txt'
    filename = '../datasets/11.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
