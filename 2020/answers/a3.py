import numpy as np

def ski(down,right,field):
    pos = (0,0)
    trees = 0
    while pos[0] < field.shape[0]:
        if field[pos] == '#':
            trees += 1
        pos = (pos[0]+down, (pos[1]+right)%field.shape[1])
    return trees

def part1(file):
    with open(file) as f:
        field = np.array([list(l.strip()) for l in f.readlines()],dtype=str)
        print(ski(1,3,field))
        
def part2(file):
    with open(file) as f:
        field = np.array([list(l.strip()) for l in f.readlines()],dtype=str)
        downs = [1,1,1,1,2]
        rights = [1,3,5,7,1]
        total = 1
        for down,right in zip(downs,rights):
            total *= ski(down,right,field)
        print(total)

def main():
    # filename = '../example.txt'
    filename = '../datasets/3.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
