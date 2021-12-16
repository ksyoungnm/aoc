# this problem was also an absolute blast. just watching the second part move
# blazingly fast is so satisfying to watch lol. very satisfying.

from collections import Counter, defaultdict
    
def part1(file):
    with open(file) as f:
        template,rules = f.read().split('\n\n')
        template = template.strip()
        rules = [r.split(' -> ') for r in rules.strip().split('\n')]
        rules = {r[0]:r[1] for r in rules}

        steps = 10

        for _ in range(steps):
            newtemp = template[0]
            for i in range(1,len(template)):
                comb = rules[template[i-1]+template[i]]
                newtemp += comb + template[i]
            template = newtemp

        cntr = Counter(template)
        print(max(cntr.values()) - min(cntr.values()))

#-------------------------------------------------------------------------------

def part2(file):
    with open(file) as f:
        template,rules = f.read().split('\n\n')
        template = template.strip()
        rules = [r.split(' -> ') for r in rules.strip().split('\n')]
        rules = {r[0]:[r[0][0]+r[1],r[1]+r[0][1]] for r in rules}
        
        pairdict = defaultdict(int)
        for i in range(1,len(template)):
            pairdict[template[i-1]+template[i]] += 1

        steps = 40
        for _ in range(steps):
            paircopy = pairdict.copy()
            for p in pairdict:
                for newp in rules[p]:
                    paircopy[newp] += pairdict[p]
                paircopy[p] -= pairdict[p]
            pairdict = paircopy
        
        elements = {}
        for pair in pairdict:
            elements[pair[0]] = 0
            elements[pair[1]] = 0

        for elem in elements:
            double = sum(val for key,val in pairdict.items() if elem in key) + pairdict[elem+elem]
            double += 1 if double % 2 == 1 else 0
            elements[elem] = double // 2

        print(max(elements.values()) - min(elements.values()))

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()