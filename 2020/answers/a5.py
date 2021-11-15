def getrow(rowstr):
    bot = 0
    top = 127
    mid = (bot+top) // 2
    for ch in rowstr:
        if ch == 'F':
            top = mid
        else:
            bot = mid+1
        mid = (bot+top) // 2
    return mid

def getcol(colstr):
    bot = 0
    top = 7
    mid = (bot+top) // 2
    for ch in colstr:
        if ch == 'L':
            top = mid
        else:
            bot = mid+1
        mid = (bot+top) // 2
    return mid

def part1(file):
    with open(file) as f:
        seats = [l.strip() for l in f.readlines()]
        ids = []
        for seat in seats:
            row = getrow(seat[:7])
            col = getcol(seat[7:])
            ids.append(row*8 + col)
        print(max(ids))

def part2(file):
    with open(file) as f:
        seats = [l.strip() for l in f.readlines()]

    ids = []
    for seat in seats:
        row = getrow(seat[:7])
        col = getcol(seat[7:])
        ids.append(row*8 + col)
    
    minid = min(ids)
    maxid = max(ids)
    for seatnum in range(minid,maxid):
        if seatnum not in ids:
            print(seatnum)

def main():
    # filename = '../example.txt'
    filename = '../datasets/5.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
