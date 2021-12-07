from collections import Counter

def part1(file):
    with open(file) as f:
        fish = Counter(map(int,f.readline().strip().split(',')))
        
        days = 256
        for _ in range(days):
            fcopy = fish.copy()
            for i in range(8,0,-1):
                fish[i-1] = fcopy[i]
            fish[6] = fish[6] + fcopy[0]
            fish[8] = fcopy[0]
        
        print(sum(fish.values()))
        
#-------------------------------------------------------------------------------

def part2(file):
    # just adjust the days value in part 1
    pass

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    # part2(filename)

if __name__ == '__main__':
    main()