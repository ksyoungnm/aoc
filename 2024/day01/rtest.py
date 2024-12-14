

def part1(filename):
    with open(filename) as f:
        list1, list2 = [],[]
        lines = [l.strip().split() for l in f.readlines()]

        for (pair0, pair1) in lines:
            list1.append(int(pair0))
            list2.append(int(pair1))

        list1.sort()
        list2.sort()

        totaldist = 0
        for (i,j) in zip(list1, list2):
            totaldist += abs(i - j)

        print(totaldist)


def part2(filename):
    with open(filename) as f:
        list1, list2 = [],[]
        lines = [l.strip().split() for l in f.readlines()]

        for (pair0, pair1) in lines:
            list1.append(int(pair0))
            list2.append(int(pair1))

        totaldist = 0
        for i in list1:
            totaldist += list2.count(i) * i

        print(totaldist)

def main():
    filename = "./example.txt"
    filename = "./data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
