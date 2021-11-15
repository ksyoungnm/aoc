import collections

def part1(file):
    with open(file) as f:
        jolts = [int(l) for l in f.readlines()]
        jolts = [0] + sorted(jolts) + [max(jolts)+3]
        jumps = [jolts[i]-jolts[i-1] for i in range(1,len(jolts))]
        counts = collections.Counter(jumps)
        print(counts[1]*counts[3])

def makechildgraph(jolts):
    jolts = [max(jolts)+3] + sorted(jolts,reverse=True) + [0]
    dchild = {}
    for i,jolt in enumerate(jolts):
        dchild[jolt] = [test for test in jolts[i+1:i+4] if (jolt-test) < 4]
    return(dchild)
    
def makedistdict(jolts,dchild):
    jolts = sorted(jolts) + [max(jolts)+3]
    ddist = {0:1}
    for jolt in jolts:
        ddist[jolt] = sum([ddist[child] for child in dchild[jolt]])
    return ddist

def part2(file):
    with open(file) as f:
        jolts = [int(l) for l in f.readlines()]
        dchild = makechildgraph(jolts)
        ddist = makedistdict(jolts,dchild)
        print(ddist[max(jolts)+3])

def main():
    filename = '../example.txt'
    filename = '../datasets/10.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
