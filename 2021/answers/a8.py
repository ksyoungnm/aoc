
def part1(file):
    with open(file) as f:
        lines = [l.strip().split(' | ')[1].split() for l in f.readlines()]
        print(sum(1 for l in lines for seg in l if len(seg) in (2,3,4,7)))

#-------------------------------------------------------------------------------

def getnum(decode,output):
    decoder = {}

    # add 1,4,7,8
    decoder[1] = next(filter(lambda x:len(x)==2,decode))
    decoder[4] = next(filter(lambda x:len(x)==4,decode))
    decoder[7] = next(filter(lambda x:len(x)==3,decode))
    decoder[8] = next(filter(lambda x:len(x)==7,decode))

    # split remaining digits into segs of len 5 and 6
    # 5: 2,3,5
    # 6: 0,6,9
    fives = [dec for dec in decode if len(dec) == 5]
    sixes = [dec for dec in decode if len(dec) == 6]

    # add 9
    nineset = set(decoder[4]).union(set(decoder[7]))
    decoder[9] = next(filter(lambda x:all(ch in x for ch in nineset), sixes))
    sixes.remove(decoder[9])
    
    # add 0 and 6
    decoder[6] = next(filter(lambda x:len(set(decoder[1])-set(x))==1,sixes))
    sixes.remove(decoder[6])
    decoder[0] = sixes[0]

    # add 5
    decoder[5] = next(filter(lambda x:len(set(decoder[6]) - set(x))==1,fives))
    fives.remove(decoder[5])

    # add 2 and 3
    decoder[3] = next(filter(lambda x:len(set(x)-set(decoder[1]))==3,fives))
    fives.remove(decoder[3])
    decoder[2] = fives[0]

    # decoding
    digdecoder = {frozenset(val):key for key,val in decoder.items()}
    finalnum = 0
    for i,dig in enumerate(output):
        finalnum += digdecoder[frozenset(dig)] * (10**(len(output) - i - 1))
    return finalnum

def part2(file):
    with open(file) as f:
        lines = [l.strip().split(' | ') for l in f.readlines()]
        decode = [l[0].split() for l in lines]
        output = [l[1].split() for l in lines]

        print(sum(getnum(d,o) for d,o in zip(decode,output)))

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()