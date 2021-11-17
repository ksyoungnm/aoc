import math

def parsetext(lines):
    notes,ticket,nearby = {},[],[]
    # flag vals: 0 for notes, 1 for my ticket, 2 for nearby
    fflag = 0
    for line in lines:
        if line == '\n':
            fflag += 1
            continue
        if fflag == 0:
            field = line.strip().split(':')[0]
            note = line.split(':')[1].strip().split(' or ')
            note = [tuple(map(int,n.split('-'))) for n in note]
            note = [set(range(n[0],n[1]+1)) for n in note]
            note = set.union(*note)
            notes[field] = note
        elif fflag == 1:
            if line.strip()[-1]!=':':
                ticket = list(map(int,line.strip().split(',')))
        elif fflag == 2:
            if line.strip()[-1]!=':':
                tick = list(map(int,line.strip().split(',')))
                nearby.append(tick)
    return notes,ticket,nearby

def getvalid(notes,nearby):
    valid = []
    possiblevals = set.union(*notes.values())
    for t in nearby:
        if set(t).issubset(possiblevals):
            valid.append(t)
    return(valid)

def part1(file):
    with open(file) as f:
        notes,ticket,nearby = parsetext(f.readlines())
        possiblevals = set.union(*notes.values())
        total = 0
        for t in nearby:
            for f in t:
                if f not in possiblevals:
                    total += f
        print(total)

def part2(file):
    with open(file) as f:
        notes,ticket,nearby = parsetext(f.readlines())
        valid = getvalid(notes,nearby)

        found = {}
        notfound = [i for i,c in enumerate(notes)]
        while len(found) < len(notes):
            for i in notfound:
                column = [v[i] for v in valid]
                checks = set(notes) - set(found)
                for c in column:
                    for n in notes:
                        if c not in notes[n]:
                            checks.remove(n)
                if len(checks) == 1:
                    field = checks.pop()
                    found[field] = i
                    notfound.remove(i)

        ids = [found[iden] for iden in found if iden[:9] == 'departure']
        print(math.prod([ticket[i] for i in ids]))
            

def main():
    # filename = 'example.txt'
    filename = 'data.txt'
    part2(filename)
    # part1(filename)

if __name__ == '__main__':
    main()