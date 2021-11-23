# kind of a fun recursion puzzle. reminds me of the war simulator i built a
# while back. anyway I've been much more enjoying these puzzles than like 18-20.

def getdecks(lines):
    deck1, deck2 = [],[]
    deckflag = True
    for line in lines:
        if line[:6] == 'Player': continue
        if line == '':
            deckflag = not deckflag
            continue
        if deckflag: deck1.append(int(line))
        else: deck2.append(int(line))
    return deck1,deck2

def part1(file):
    with open(file) as f:
        alllines = [l.strip() for l in f.readlines()]
        deck1, deck2 = getdecks(alllines)

        while len(deck1) > 0 and len(deck2) > 0:
            c1 = deck1.pop(0)
            c2 = deck2.pop(0)
            if c1 > c2:
                deck1 += [c1,c2]
            else:
                deck2 += [c2,c1]

        winner = deck1 if len(deck1) > 0 else deck2

        print(sum([(len(winner)-i)*card for i,card in enumerate(winner)]))


#-------------------------------------------------------------------------------
def playRecursive(d1,d2):
    history = set()
    while len(d1) > 0 and len(d2) > 0:
        if (tuple(d1),tuple(d2)) in history:
            return('p1',d1,d2)

        history.add((tuple(d1),tuple(d2)))

        c1 = d1.pop(0)
        c2 = d2.pop(0)

        if (len(d1) >= c1 and len(d2) >= c2):
            result = playRecursive(d1[:c1],d2[:c2])
            if result[0] == 'p1': d1 += [c1,c2]
            else: d2 += [c2,c1]

        else:
            if c1 > c2:
                d1 += [c1,c2]
            else:
                d2 += [c2,c1]

    winner = 'p1' if len(d1) > 0 else 'p2'

    return(winner,d1,d2)


def part2(file):
    with open(file) as f:
        alllines = [l.strip() for l in f.readlines()]
        deck1, deck2 = getdecks(alllines)

        result = playRecursive(deck1,deck2)
        winner = result[1] if result[0] == 'p1' else result[2]
        print(sum([(len(winner)-i)*card for i,card in enumerate(winner)]))

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()