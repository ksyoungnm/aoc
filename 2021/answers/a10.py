
def part1(file):
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
        badchs = []
        for line in lines:
            stack = []
            for ch in line:
                if ch in '([{<':
                    stack.append(ch)
                else:
                    match ch:
                        case ')': test = '('
                        case ']': test = '['
                        case '}': test = '{'
                        case '>': test = '<'
                    if test != stack.pop():
                        badchs.append(ch)
                        break

        scores = {')':3,']':57,'}':1197,'>':25137}
        print(sum(scores[bch] for bch in badchs))

#-------------------------------------------------------------------------------

def part2(file):
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
        rem_stacks = []
        for line in lines:
            addflag = True
            stack = []
            for ch in line:
                if ch in '([{<':
                    stack.append(ch)
                else:
                    match ch:
                        case ')': test = '('
                        case ']': test = '['
                        case '}': test = '{'
                        case '>': test = '<'
                    if test != stack.pop():
                        addflag = False
                        break
            if addflag:
                rem_stacks.append(stack)

        scorelist = []
        scores = {'(':1,'[':2,'{':3,'<':4}
        for stk in rem_stacks:
            s = 0
            for ch in stk[::-1]:
                s = s*5 + scores[ch]
            scorelist.append(s)

        print(sorted(scorelist)[len(scorelist)//2])

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()