
def part1(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]

        charsets = [set()]
        index = 0
        for line in lines:
            if len(line) > 0:
                charsets[index] = charsets[index].union(set(line))
            else:
                index += 1
                charsets.append(set())
        print(sum(map(len,charsets)))

def part2(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
        
        candidates = set(lines[0])
        counts = []
        for i,line in enumerate(lines):
            if len(line) > 0:
                candidates = candidates.intersection(set(line))
            else:
                counts.append(len(candidates))
                candidates = set(lines[i+1])

        if lines[-1] != '':
            counts.append(len(candidates))
        print(sum(counts))

def main():
    # filename = '../example.txt'
    filename = '../datasets/6.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
