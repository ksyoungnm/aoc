# Probably the jankiest answer i've written so far. this could be made much
# nicer to look at but eh haha

import itertools

def getmask(line):
    # ormask to set 1s, andmask to set 0s
    ormask = 0
    andmask = 2**36 -1
    for i,ch in enumerate(line):
        if ch == '0':
            andmask ^= 1 << (35-i)
        if ch == '1':
            ormask |= 1 << (35-i)
    return(ormask,andmask)

def part1(file):
    with open(file) as f:
        memarray = {}
        for line in f.readlines():
            if line[:4] == 'mask':
                ormask,andmask = getmask(line.strip().split()[2])
            else:
                address = int(line.split('[')[1].split(']')[0])
                val = int(line.split()[2]) & andmask | ormask
                memarray[address] = val
        print(sum(memarray.values()))

def setbit(num,i,bit):
    targetbit = num & (1 << i) != 0
    if targetbit == bit:
        return num
    else:
        if targetbit:
            return num & ~(1 << i)
        else:
            return num + (1 << i)

def getaddresses(baseaddress,mask):
    ormask = 0
    floatis = []
    for i,ch in enumerate(mask):
        if ch == '1': ormask |= 1 << (35-i)
        if ch == 'X': floatis.append(i)
    baseaddress |= ormask
    addresses = []
    for combo in itertools.product((0,1),repeat=len(floatis)):
        addy = baseaddress
        for i,bit in enumerate(combo):
            addy = setbit(addy,35-floatis[i],bit)
        addresses.append(addy)
    
    return(addresses)

def part2(file):
    with open(file) as f:
        memarray = {}
        for line in f.readlines():
            if line[:4] == 'mask':
                mask = line.strip().split()[2]
            else:
                baseaddress = int(line.split('[')[1].split(']')[0])
                addresses = getaddresses(baseaddress,mask)
                val = int(line.split()[2])
                for addy in addresses:
                    memarray[addy] = val
        print(sum(memarray.values()))    

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()