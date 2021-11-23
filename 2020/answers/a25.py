# haha turns out this puzzle had the easiest answer: reading the documentation
# on the builtin pow function, in order to just quickly check through every
# possible key. is there a better way? maybe


def part1(file):
    with open(file) as f:
        ckey,dkey = [int(l.strip()) for l in f.readlines()]
        print(ckey,dkey)

        i = 0
        while True:
            if i % 1000000 == 0:
                print(i)
            t = pow(7,i,20201227)
            if t == ckey:
                print(i)
                loop = i
                pkey = dkey
                break
            if t == dkey:
                print(i)
                loop = i
                pkey = ckey
                break
            i+=1

        print(pow(pkey,loop,20201227))

        
#-------------------------------------------------------------------------------


def part2(file):
    with open(file) as f:
        pass

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    # part2(filename)

if __name__ == '__main__':
    main()