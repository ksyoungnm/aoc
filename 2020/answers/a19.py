# oof okay these are getting jankier by the second. had to hard code some rules in here,
# but it works. also def used some domain knowledge that I wouldn't ve shocked if it was
# specific to this set of problems. anyway.

from collections import defaultdict
from itertools import product

def makeruledict(rules):
    ruled = {}
    inhd = defaultdict(set)
    for rule in rules:
        name,reqs = rule.split(':')
        reqs = reqs.strip(' "')
        if reqs != 'a' and reqs != 'b':
            reqs = reqs.split(' | ')
            reqs = [r.split() for r in reqs]
            for subr in reqs:
                for r in subr:
                    inhd[r].add(name)
        ruled[name] = reqs

    return ruled, inhd

def getlen(rule,ruled):
    if ruled[rule] == 'a' or ruled[rule] == 'b':
        return set((1,))
    else:
        combo = set()
        for ruleor in ruled[rule]:
            rulelen = []
            for r in ruleor:
                rulelen.append(getlen(r,ruled))
            combo = combo.union(set(map(sum,product(*rulelen))))
        return combo

def checkrule(string,rule,ruled,lend):
    if len(string) != lend[rule]:
        return False
    elif ruled[rule] == 'a' or ruled[rule] == 'b':
        if string == ruled[rule]:
            return True
        else:
            return False
    else:
        for ruleor in ruled[rule]:
            splt = 0
            checks = []
            for r in ruleor:
                if checkrule(string[splt:splt+lend[r]],r,ruled,lend):
                    checks.append(1)
                else:
                    checks.append(0)
                splt += lend[r]

            if sum(checks) == len(ruleor):
                return True
        return False


def part1(file):

    with open(file) as f:
        alllines = [l.strip() for l in f.readlines()]
        rulesidx = alllines.index('')
        rules = alllines[:rulesidx]
        tocheck = alllines[rulesidx+1:]
        
        ruled, inhd = makeruledict(rules)
        # after some detective work, can confidently say that
        # each rule has only a single acceptable length. i built
        # the getlen function to return sets of acceptable lengths,
        # but since each rule has only a single length, can just
        # pop and use the integer vals in this dictionary.
        lend = {key:getlen(key,ruled).pop() for key in ruled}
        total = 0
        for line in tocheck:
            if checkrule(line,'0',ruled,lend):
                total += 1
        print(total)



#-------------------------------------------------------------------------------    

def checkrule2(string,rule,ruled,lend):
    #gonna hard code rules for 0,8,and 11 here.
    if string == '':
        return False
    elif rule == '0':
        if len(string) % lend['42'] != 0:
            return False
        else:
            starti = lend['42']
            while starti < len(string):
                if checkrule2(string[:starti],'8',ruled,lend) and checkrule2(string[starti:],'11',ruled,lend):
                    return True
                starti += lend['42']
            return False

    elif rule == '8':
        if len(string) % lend['42'] != 0:
            return False
        else:
            starti = 0
            while starti < len(string):
                if not checkrule2(string[starti:starti+lend['42']],'42',ruled,lend):
                    return False
                starti += lend['42']
            return True
        
    elif rule == '11':
        if len(string) % (lend['42'] + lend['31']) != 0:
            return False
        else:
            midp = len(string) // 2
            starti = 0
            while starti < midp:
                s1check = string[starti:starti+lend['42']]
                s2check = string[starti+midp:starti+midp+lend['31']]
                if not (checkrule2(s1check,'42',ruled,lend) and checkrule2(s2check,'31',ruled,lend)):
                    return False
                starti += lend['42']
            return True

    elif len(string) != lend[rule]:
        return False
    elif ruled[rule] == 'a' or ruled[rule] == 'b':
        if string == ruled[rule]:
            return True
        else:
            return False
    else:
        for ruleor in ruled[rule]:
            splt = 0
            checks = []
            for r in ruleor:
                if checkrule2(string[splt:splt+lend[r]],r,ruled,lend):
                    checks.append(1)
                else:
                    checks.append(0)
                splt += lend[r]

            if sum(checks) == len(ruleor):
                return True
        return False

def part2(file):
    with open(file) as f:
        alllines = [l.strip() for l in f.readlines()]
        rulesidx = alllines.index('')
        rules = alllines[:rulesidx]
        tocheck = alllines[rulesidx+1:]
        
        ruled, inhd = makeruledict(rules)
        lend = {key:getlen(key,ruled).pop() for key in ruled}

        total = 0
        for line in tocheck:
            if checkrule2(line,'0',ruled,lend):
                total += 1
        print(total)
            

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()