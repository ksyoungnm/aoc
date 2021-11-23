# this one was also more fun than hard. especially enjoyable was the little
# hexagon coordinate system. not as hard as some of the earlier puzzles

def getDirections(line):
    twoflag = False
    directions = []
    for i,ch in enumerate(line):
        if twoflag:
            twoflag = False
        elif ch == 'n' or ch == 's':
            directions.append(line[i:i+2])
            twoflag = True
        else:
            directions.append(ch)
    return directions

def move(tile,d):
    if d == 'ne': return (tile[0]+0, tile[1]+1, tile[2]+1)
    if d == 'e': return (tile[0]-1, tile[1]+1, tile[2]+0)
    if d == 'se': return (tile[0]-1, tile[1]+0, tile[2]-1)
    if d == 'sw': return (tile[0]+0, tile[1]-1, tile[2]-1)
    if d == 'w': return (tile[0]+1, tile[1]-1, tile[2]+0)
    if d == 'nw': return (tile[0]+1, tile[1]+0, tile[2]+1)

def getTile(directions):
    tile = (0,0,0)
    for d in directions:
        tile = move(tile,d)
    return tile

def part1(file):
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
        directions = [getDirections(l) for l in lines]
        
        tiles = {}
        for d in directions:
            tile = getTile(d)
            if tile in tiles:
                tiles[tile] = not tiles[tile]
            else:
                tiles[tile] = True

        print(sum(tiles.values()))
        

#-------------------------------------------------------------------------------
def getNeighbors(t):
    return [ move(t,'ne'),move(t,'e'),move(t,'se'),
             move(t,'nw'),move(t,'w'),move(t,'sw') ]

def countNeighbors(t,tiles):
    count = 0
    for n in getNeighbors(t):
        try:
            count += tiles[n]
        except KeyError:
            pass
    return count

def updateTiles(tiles):
    # true = black, false = white
    newtiles = tiles.copy()
    
    for tile in (t for t,bw in tiles.items() if bw):
        for n in getNeighbors(tile):
            if n not in newtiles:
                newtiles[n] = False
    
    tiles = newtiles.copy()
    
    for tile,bw in tiles.items():
        count = countNeighbors(tile,tiles)
        if bw:
            if count == 0 or count > 2:
                newtiles[tile] = not newtiles[tile]
        else:
            if count == 2:
                newtiles[tile] = not newtiles[tile]

    return(newtiles)


def part2(file):
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
        directions = [getDirections(l) for l in lines]
        
        tiles = {}
        for d in directions:
            tile = getTile(d)
            if tile in tiles:
                tiles[tile] = not tiles[tile]
            else:
                tiles[tile] = True

        for _ in range(100):
            tiles = updateTiles(tiles)
        
        print(sum(tiles.values()))

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    # part2(filename)

if __name__ == '__main__':
    main()