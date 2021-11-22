# dear lord if you value you sanity do not try to untangle any of this mess. its
# super hobbled together, lots of different things happening that for sure could
# handled better but I built this while exhausted and it really shows. also holy
# crap this was a hard puzzle


import numpy as np
from collections import defaultdict
from math import prod

def getEdgeShareDict(tiles):
    edges = {}
    for tileid,tile in tiles.items():
        e1 = tile[0,:]
        e2 = tile[:,9]
        e3 = np.flip(tile[9,:])
        e4 = np.flip(tile[:,0])
        for i,e in enumerate((e1,e2,e3,e4)):
            if tuple(e) in edges:
                edges[tuple(e)].append((tileid, i, True))
            elif tuple(np.flip(e)) in edges:
                edges[tuple(np.flip(e))].append((tileid, i, False))
            else:
                edges[tuple(e)] = [(tileid, i, True)]
    return edges
def getcorners(tiles,edgeShare):
    uEdges = {}
    for tileid,tile in tiles.items():
        count = 0

        e1 = tile[0,:]
        e2 = tile[:,9]
        e3 = np.flip(tile[9,:])
        e4 = np.flip(tile[:,0])

        for e in ((e1,e2,e3,e4)):
            if tuple(e) in edgeShare:
                if len(edgeShare[tuple(e)]) == 1:
                    count += 1
            else:
                if len(edgeShare[tuple(np.flip(e))]) == 1:
                    count += 1

        uEdges[tileid] = count

    corners = [keyid for keyid,count in uEdges.items() if count == 2]
    return corners
def part1(file):
    with open(file) as f:
        alllines = [l.strip() for l in f.readlines()]
        tiles = {}
        for i,l in enumerate(alllines):
            if l[0:4] == 'Tile':
                key = int(l.split()[1].strip(':'))
                val = np.array([list(li) for li in alllines[i+1:i+11]],dtype=str)
                tiles[key] = val
        edgeShare = getEdgeShareDict(tiles)
        print(getcorners(tiles,edgeShare))

#-------------------------------------------------------------------------------

def orient(tileid,tiles,edgeShare):
    tile = tiles[tileid]
    e0 = tile[0,:]
    e1 = tile[:,9]
    e2 = np.flip(tile[9,:])
    e3 = np.flip(tile[:,0])
    uniques = []
    for i,e in enumerate((e0,e1,e2,e3)):
        if tuple(e) in edgeShare:
            if len(edgeShare[tuple(e)]) == 1:
                uniques.append(i)
    if uniques == [0,1]: return 4
    if uniques == [1,2]: return 7
    if uniques == [2,3]: return 6
    if uniques == [3,0]: return 5
    if uniques == [1,0]: return 3
    if uniques == [2,1]: return 2
    if uniques == [3,2]: return 1
    if uniques == [0,3]: return 0
def insert(img,idx,idy,tile,orient):
    # print(idx,idy)
    if orient == 1: tile = np.rot90(tile,k=3)
    if orient == 2: tile = np.rot90(tile,k=2)
    if orient == 3: tile = np.rot90(tile,k=1)
    if orient == 4: tile = np.rot90(np.flipud(tile),k=2)
    if orient == 5: tile = np.rot90(np.flipud(tile),k=3)
    if orient == 6: tile = np.flipud(tile)
    if orient == 7: tile = np.rot90(np.flipud(tile),k=1)

    newimg = np.copy(img)
    dx,dy = tile.shape
    newimg[idx:idx+dx,idy:idy+dy] = tile
    return newimg
def match(tileid,edgeid,edgeShare):
    # given a tileid and edgeid, returns the complementary boundary. also true
    # if they run antiparallel and false otherwise.
    for val in edgeShare.values():
        lrist = [(v[0],v[1]) for v in val]
        if (tileid,edgeid) in lrist:
            notidx = lrist.index((tileid,edgeid))
            newid,newedge,tf = val[(notidx+1)%2]
            return (newid,newedge,tf!=val[notidx][2])
def getEdgeID(rowcol,orient):
    if rowcol == 'col':
        if orient == 0: return 1
        if orient == 1: return 0
        if orient == 2: return 3
        if orient == 3: return 2
        if orient == 4: return 3
        if orient == 5: return 2
        if orient == 6: return 1
        if orient == 7: return 0
    if rowcol == 'row':
        if orient == 0: return 2
        if orient == 1: return 1
        if orient == 2: return 0
        if orient == 3: return 3
        if orient == 4: return 2
        if orient == 5: return 1
        if orient == 6: return 0
        if orient == 7: return 3
def getOrient(rowcol,edgeid,oppsame,updown):
    if rowcol == 'col':
        if edgeid == 0:
            if oppsame == updown: return 5
            else: return 3
        if edgeid == 1:
            if oppsame == updown: return 4
            else: return 2
        if edgeid == 2:
            if oppsame == updown: return 7
            else: return 1
        if edgeid == 3:
            if oppsame == updown: return 6
            else: return 0
    if rowcol == 'row':
        if edgeid == 0:
            if oppsame == updown: return 4
            else: return 0
        if edgeid == 1:
            if oppsame == updown: return 7
            else: return 3
        if edgeid == 2:
            if oppsame == updown: return 6
            else: return 2
        if edgeid == 3:
            if oppsame == updown: return 5
            else: return 1
def buildimage(tiles,edgeShare,corner):
    td = int(len(tiles)**0.5)
    img = np.full((td*8,td*8),'0',dtype=str)
    
    ot = orient(corner,tiles,edgeShare)
    prevrow0 = (corner,ot)
    prevcol = (corner,ot)

    img = insert(img,0,0,tiles[corner][1:-1,1:-1],ot)
    # print(prevcol)
    # newid,eid,oppsame = match(prevcol[0],getEdgeID('col',prevcol[1]),edgeShare)
    # print(newid,eid,oppsame)
    # print(getOrient(eid,oppsame,prevcol[1]>3))
    for rowi in range(0,td):
        for colj in range(1,td):
            newid,eid,oppsame = match(prevcol[0],getEdgeID('col',prevcol[1]),edgeShare)
            newot = getOrient('col',eid,oppsame,prevcol[1]>3)
            img = insert(img,rowi*8,colj*8,tiles[newid][1:-1,1:-1],newot)
            prevcol = (newid,newot)
            # print(prevcol,prevrow0)
        if rowi < (td - 1):
            newid,eid,oppsame = match(prevrow0[0],getEdgeID('row',prevrow0[1]),edgeShare)
            # print(newid,eid,oppsame)
            newot = getOrient('row',eid,oppsame,prevrow0[1]>3)
            # print(newot)
            img = insert(img,(rowi+1)*8,0,tiles[newid][1:-1,1:-1],newot)
            prevcol = (newid,newot)
            prevrow0 = (newid,newot)
            # print(prevcol,prevrow0)
    return img
def checkMonster(img,idx,idy):
    midxs = [(1,0),(2,1),(2,4),(1,5),(1,6),(2,7),(2,10),(1,11),(1,12),(2,13),
            (2,16),(1,17),(0,18),(1,18),(1,19)]
    checks = []
    for mi in midxs:
        if img[idx+mi[0],idy+mi[1]] == '#':
            checks.append(1)
    if sum(checks) == len(midxs):
        return True
    else:
        return False
def findMonsters(img):
    count = 0
    for i in range(img.shape[0] - 2):
        for j in range(img.shape[1] - 19):
            if checkMonster(img,i,j):
                count += 1
    return count
def countWaves(img):
    checksir = np.copy(img)
    midxs = [(1,0),(2,1),(2,4),(1,5),(1,6),(2,7),(2,10),(1,11),(1,12),(2,13),
            (2,16),(1,17),(0,18),(1,18),(1,19)]

    for i in range(img.shape[0] - 2):
        for j in range(img.shape[1] - 19):
            if checkMonster(img,i,j):
                for mi in midxs:
                    checksir[i+mi[0],j+mi[1]] = '.'
    
    return np.sum(checksir == np.full_like(checksir,'#'))
def part2(file):
    with open(file) as f:
        alllines = [l.strip() for l in f.readlines()]
        tiles = {}
        for i,l in enumerate(alllines):
            if l[0:4] == 'Tile':
                key = int(l.split()[1].strip(':'))
                val = np.array([list(li) for li in alllines[i+1:i+11]],dtype=str)
                tiles[key] = val


        edgeShare = getEdgeShareDict(tiles)
        corners = getcorners(tiles,edgeShare)
        img = buildimage(tiles,edgeShare,corners[0])

        transls = (img,
            np.rot90(img,k=3),
            np.rot90(img,k=2),
            np.rot90(img,k=1),
            np.rot90(np.flipud(img),k=2),
            np.rot90(np.flipud(img),k=3),
            np.flipud(img),
            np.rot90(np.flipud(img),k=1))

        for i,trans in enumerate(transls):
            if findMonsters(trans) > 0:
                print(countWaves(trans))
                break

#-------------------------------------------------------------------------------

def main():
    np.set_printoptions(linewidth=100000)
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()