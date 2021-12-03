
def part1(file):
    with open(file) as f:
        diag = [l.strip() for l in f.readlines()]

        gamma = 0
        epsi = 0

        for i in range(len(diag[0])):
            test = sum([int(d[i]) for d in diag])

            if test > len(diag)/2:
                gamma += 2**(len(diag[0]) - i - 1)
            else:
                epsi += 2**(len(diag[0]) - i - 1)

        print(gamma*epsi)

#-------------------------------------------------------------------------------

def getRating(diag,rating):
    for i in range(len(diag[0])):
        test = sum((int(d[i]) for d in diag))
        select = '0' if ((test < len(diag)/2) == (rating == 'oxy')) else '1'
        diag = [d for d in diag if d[i] == select]
        if len(diag) == 1:
            return int(diag[0],2)

def part2(file):
    with open(file) as f:
        diag = [l.strip() for l in f.readlines()]
        
        oxy = getRating(diag,'oxy')
        co2 = getRating(diag,'co2')
        print(oxy*co2)
        
#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()