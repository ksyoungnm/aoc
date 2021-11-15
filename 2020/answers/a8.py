
def runprogram(program):
    accumulator = 0
    pc = 0
    history = []

    while not (pc == len(program)):
        ins,val = program[pc]
        
        history.append(pc)
        if ins == 'nop':
            pc += 1
        if ins == 'acc':
            accumulator += val
            pc += 1
        if ins == 'jmp':
            pc += val

        if (pc > len(program) or pc < 0 or pc in history):
            return (False, accumulator)

    return (True, accumulator)

def part1(file):
    with open(file) as f:
        program = [l.strip().split() for l in f.readlines()]
        program = [(ins,int(val)) for ins,val in program]
        print(runprogram(program)[1])

def part2(file):
    with open(file) as f:
        program = [l.strip().split() for l in f.readlines()]
        program = [(ins,int(val)) for ins,val in program]
        
    for i,(ins,val) in enumerate(program):
        success = False
        if ins == 'jmp':
            test = program[:i] + [('nop',val)] + program[i+1:]
            success,accum = runprogram(test)
        if ins == 'nop':
            test = program[:i] + [('jmp',val)] + program[i+1:]
            success,accum = runprogram(test)
        if success:
            print(accum)
            return

def main():
    filename = '../example.txt'
    filename = '../datasets/8.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
