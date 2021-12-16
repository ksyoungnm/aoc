# this also was a fun one, but also kinda hard. i originally wrote up a jank
# version of dijkstra but it was hella slow, so i implemented this new one. it
# relies on the fact that moving from the top left to bottom right we will
# generally increase the distance, and the fact that the highest number possible
# is 9 limits the amount we have to backtrack. anyway. fun puzzle for sure

import numpy as np

def getneighbs(p,mind,maxd):
    neighbs = []
    neighbs.append((p[0]-1,p[1]))
    neighbs.append((p[0]+1,p[1]))
    neighbs.append((p[0],p[1]-1))
    neighbs.append((p[0],p[1]+1))
    neighbs = [n for n in neighbs if (mind <= n[0] < maxd) and (mind <= n[1] < maxd)]
    for n in neighbs:
        yield n

def getprevrow(p,mind,maxd):
    neighbs = []
    neighbs.append((p[0]-1,p[1]))
    neighbs.append((p[0],p[1]-1))
    neighbs = [n for n in neighbs if (mind <= n[0] < maxd) and (mind <= n[1] < maxd)]
    return neighbs

def newgraph(chitin):
    dists = np.zeros_like(chitin)
    rows = 2*chitin.shape[0] - 1
    for i in range(1,rows):
        cRange = range(i+1) if i <= rows//2 else range(i-chitin.shape[0]+1,chitin.shape[0])
        nextRow = [(i-p,p) for p in cRange]

        for p in nextRow:
            neighbs = getprevrow(p,0,chitin.shape[0])
            dists[p] = min(dists[n] + chitin[p] for n in neighbs)

            queue = [(n,p) for n in neighbs]
            while len(queue) > 0:
                node,source = queue.pop()
                if dists[node] > dists[source] + chitin[node]:
                    dists[node] = dists[source] + chitin[node]
                    for oln in getneighbs(node,0,chitin.shape[0]):
                        queue.append((oln,node))
    print(dists[(chitin.shape[0]-1,chitin.shape[1]-1)])



def part1(file):
    chitin = np.genfromtxt(file,dtype=int,delimiter=1)
    newgraph(chitin)

#-------------------------------------------------------------------------------

def part2(file):
    chitin = np.genfromtxt(file,dtype=int,delimiter=1)
    ogdims = chitin.shape
    for _ in range(4):
        newchitin = chitin[:,-ogdims[1]:] + 1
        newchitin[newchitin==10] = 1
        chitin = np.concatenate((chitin,newchitin),axis=1)
    for _ in range(4):
        newchitin = chitin[-ogdims[0]:,:] + 1
        newchitin[newchitin==10] = 1
        chitin = np.concatenate((chitin,newchitin),axis=0)

    newgraph(chitin)

#-------------------------------------------------------------------------------

def main():
    np.set_printoptions(linewidth=100000)
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    # part2(filename)

if __name__ == '__main__':
    main()
