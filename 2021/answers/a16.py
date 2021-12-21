# also pretty fun! only ~annoying bit is when converting to the binary string
# representation python gets rid of leading zeros, but after chewing on that for
# porbably longer than i should have, rest was ok. could probs make this more
# efficient by not making the poor thing create a ton of recursive copies of the
# string but eh who has the time

from math import prod

def parse(pack):
    version = int(pack[:3],2)
    typeid = int(pack[3:6],2)

    if typeid == 4:
        i = 6
        bins = []
        while True:
            bins.append(pack[i+1:i+5])
            i += 5
            if pack[i-5] == '0':
                break
        value = int(''.join(bins),2)
        return value,version,i

    else:
        valrets,verrets,lenrets = [],[],[]
        lentype = int(pack[6])

        if not lentype:
            bits = int(pack[7:22],2)
            i = 22
        else:
            subpacks = int(pack[7:18],2)
            i = 18

        while ((not lentype) and (i < bits + 22)) or (lentype and (subpacks > 0)):
            valret,verret,lenret = parse(pack[i:])
            valrets.append(valret)
            verrets.append(verret)
            lenrets.append(lenret)
            i += lenrets[-1]
            if lentype:
                subpacks -= 1

        match typeid:
            case 0: value = sum(valrets)
            case 1: value = prod(valrets)
            case 2: value = min(valrets)
            case 3: value = max(valrets)
            case 5: value = 1 if valrets[0] >  valrets[1] else 0
            case 6: value = 1 if valrets[0] <  valrets[1] else 0
            case 7: value = 1 if valrets[0] == valrets[1] else 0

        if not lentype:
            return value, version + sum(verrets), 22 + sum(lenrets)
        else:
            return value, version + sum(verrets), 18 + sum(lenrets)


def part1(file):
    with open(file) as f:
        line = f.readline()
        binstr = bin(int(line,16))[2:]
        while len(binstr) % 4 != 0:
            binstr = '0' + binstr
        i = 0
        while line[i] == '0':
            binstr = '0000' + binstr
            i += 1
        print(parse(binstr))

#-------------------------------------------------------------------------------

def part2(file):
    pass

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    # part2(filename)

if __name__ == '__main__':
    main()
