import itertools

def checksum(target,available):
    # given a set of available integers and a target, check if the target is 
    # expressable as the sum of two available integers. lookout, it's a bool
    # use combinations to avoid testing (i,i) and the (i,j)/(j,i) redundancy
    return len([1 for p in itertools.combinations(available,2) if sum(p) == target]) > 0

def part1(file):
    with open(file) as f:
        nums = [int(l) for l in f.readlines()]

    preamble = 25
    for i in range(preamble,len(nums)):
        if not checksum(nums[i],nums[i-preamble:i]):
            print(nums[i])
            return

def part2(file):
    with open(file) as f:
        nums = [int(l) for l in f.readlines()]
    
    preamble = 25
    for i in range(preamble,len(nums)):
        if not checksum(nums[i],nums[i-preamble:i]):
            target = nums[i]
            break

    for i,j in itertools.combinations(range(len(nums)),2):
        if sum(nums[i:j]) == target:
            ma = max(nums[i:j]); mi = min(nums[i:j])
            print(ma+mi)
            break

def main():
    filename = '../example.txt'
    filename = '../datasets/9.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
