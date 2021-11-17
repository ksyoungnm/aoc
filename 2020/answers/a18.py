# we love miles of painstaking if else logic on this channel. im sure this is
# also riddled with inefficiencies lmao

def getopsfields(line):
    ops = []
    fields = []
    current = ''
    inparen = 0
    for ch in line:
        if ch == '(':
            inparen += 1
            if inparen > 1:
                current += ch
        elif inparen > 0:
            if ch == ')':
                if inparen == 1:
                    fields.append(current)
                    current = ''
                    inparen -= 1
                else:
                    current += ch
                    inparen -= 1
            else:
                current += ch
        elif ch == '+' or ch == '*':
            ops.append(ch)
        elif ch == ' ':
            if current != '':
                fields.append(current)
                current = ''
        else:
            current += ch
    if current != '':
            fields.append(current)
    return(ops,fields)

def evaluate(line):
    ops,fields = getopsfields(line)
    if len(fields) == 1 and len(fields[0].split()) == 1:
        return(int(fields[0]))
    else:
        total = evaluate(fields[0])
        for i,op in enumerate(ops):
            if op == '+':
                total += evaluate(fields[i+1])
            else:
                total *= evaluate(fields[i+1])
        return(total)

def part1(file):
    with open(file) as f:
        print(sum([evaluate(l) for l in f.readlines()]))

#-------------------------------------------------------------------------------    
def evaluate2(line):
    ops,fields = getopsfields(line)
    if len(fields) == 1 and len(fields[0].split()) == 1:
        return(int(fields[0]))
    else:
        while '+' in ops:
            i = ops.index('+')
            ops = ops[:i] + ops[i+1:]
            fields = fields[:i] + [str(evaluate2(fields[i]) + evaluate2(fields[i+1]))] + fields[i+2:]
        # print(ops,fields)
        total = evaluate2(fields[0])
        for i,op in enumerate(ops):
            total *= evaluate2(fields[i+1])
        return total
        

def part2(file):
    with open(file) as f:
        # l = '1 + 2 * 3 + 4 * 5 + 6'
        # print(evaluate2(l))
        test = [evaluate2(l) for l in f.readlines()]
        print(sum(test))
            

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()