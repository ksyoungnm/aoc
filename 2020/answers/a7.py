import re

def parsebagline(line):
    # returns a tuple of the form ('color',{dictionary of contained bags & counts}) to
    # be used as key:val pairs in a bags dictionary that captures all containment rules
    color,other = re.split(' bags ', line, maxsplit=1)
    other = other.replace('contain ', '')
    if other == 'no other bags.':
        other = {}
    else:
        other = re.findall(r'[1-9]+ \w+ \w+',other)
        other = {''.join([chunk.split()[1], ' ', chunk.split()[2]]):int(chunk.split()[0]) for chunk in other}

    return color,other

def containsgold(bag,collection):
    # Auxiliary for part 1.
    # Recursive function that given a bag and the dictionary with all the bag
    # containment rules returns True if that bag eventually contains a shiny gold
    # bag. Super inefficient due to many redundant checks but it still finishes 
    # in less than a second so ~good enough~
    if collection[bag] == []:
        return False
    if 'shiny gold' in collection[bag]:
        return True
    
    for newbag in collection[bag]:
        if containsgold(newbag,collection):
            return True
    return False

def part1(file):
    with open(file) as f:
        bags = dict([parsebagline(l.strip()) for l in f.readlines()])
        count = 0
        for bag in bags:
            if containsgold(bag,bags):
                count+=1
        print(count)

def countnested(bag,collection):
    # Auxiliary for part 2.
    # See above. Given a bag and the dict of containment rules, returns the number
    # of bags that must be included inside that bag. recursive, and also a ton
    # of inefficient & redundant calls 
    if len(collection[bag]) == 0:
        return 0
    else:
        total = 0
        for key,val in collection[bag].items():
            total += (countnested(key,collection)+1)*val
        return total

def part2(file):
    with open(file) as f:
        bags = dict([parsebagline(l.strip()) for l in f.readlines()])
    
    print(countnested('shiny gold', bags))

def main():
    filename = '../example.txt'
    filename = '../datasets/7.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
