
def part1(file):
    with open(file) as f:
        nums = [int(i) for i in f.readline().split(',')]
        direct = {num:(i+1) for i,num in enumerate(nums)}
        lastspoken = nums[-1]
        turn = len(nums)

        while turn < 30000000:
            turn += 1
            if lastspoken not in direct:
                speak = 0
            else:
                speak = turn - 1 - direct[lastspoken]
            direct[lastspoken] = turn - 1
            lastspoken = speak
        
        print(lastspoken)

        

def main():
    # filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part1(filename)

if __name__ == '__main__':
    main()