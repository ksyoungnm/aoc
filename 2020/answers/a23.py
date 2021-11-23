# this one is a fun puzzle too! unsurprisingly the list approach i took in part 1
# was too slow for part 2, so i took a dictionary/linked list type approach
# for the speed up. i liked this puzzle a ton

def getidx(i,mod):
    return i % mod
def getslice(cups,start,stop):
    start = getidx(start,len(cups))
    stop = getidx(stop,len(cups))
    if start > stop:
        toreturn = cups[start:] + cups[:stop]
    else:
        toreturn = cups[start:stop]
    return toreturn

def move(cups,cidx):

    wrap = max(cups)

    targets = getslice(cups,cidx,cidx+4)
    current,targets = targets[0], targets[1:]

    cups = [c for c in cups if c not in targets]
    
    dest = (current - 1) if current != 1 else wrap
    while dest not in cups:
        dest = (dest - 1) if dest != 1 else wrap

    didx = cups.index(dest)
    cups = cups[:didx+1] + targets + cups[didx+1:]

    nextcidx = (cups.index(current) + 1) % len(cups)
    return cups, nextcidx


def part1(file):
    with open(file) as f:
        cups = list(map(int,f.readline().strip()))
        cidx = 0

        for _ in range(100):
            cups,cidx = move(cups,cidx)

        print(cups,cidx)


#-------------------------------------------------------------------------------
def movelld(cups,current,iters):

    for _ in range(iters):
        t1 = cups[current]
        t2 = cups[t1]
        t3 = cups[t2]
        t4 = cups[t3]

        cups[current] = t4

        dest = current - 1 if current > 1 else max(cups)
        while dest in (t1,t2,t3):
            dest = dest - 1 if dest > 1 else max(cups)

        d1 = cups[dest]

        cups[dest] = t1
        cups[t3] = d1

        current = cups[current]

    past1 = cups[1]
    past2 = cups[past1]
    print(past1*past2)



def part2(file):
    with open(file) as f:
        cups = list(map(int,f.readline().strip()))
        cups = cups + list(range(10,1000001))
        cupd = {c:cups[(i+1)%len(cups)] for i,c in enumerate(cups)}
        movelld(cupd,cups[0],10000000)
        

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()