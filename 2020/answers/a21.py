# wow this puzzle was much easier than the others before lmao. ah well. good
# to have an easy one every now and again.

def part1(file):
    with open(file) as f:
        lines = [l.strip().split('(contains ') for l in f.readlines()]
        lines = [[l[0].strip(),l[1].strip(')')] for l in lines]
        allergens = {}
        for line in lines:
            for aller in line[1].split():
                aller = aller.strip(',')
                
                if aller not in allergens:
                    allergens[aller] = set(line[0].split())
                else:
                    allergens[aller] = allergens[aller].intersection(set(line[0].split()))
        

        for _ in range(8):
            for aller,possib in allergens.items():
                if len(possib) == 1:
                    for all2 in allergens:
                        if all2 != aller:
                            allergens[all2] = allergens[all2] - possib
        badigs = set.union(*allergens.values())
        
        # uncomment this for part 1 solution

        # count = 0
        # for line in lines:
        #     for word in line[0].split():
        #         if word not in badigs:
        #             count += 1

        # print(count)

        # uncomment this for part 2 solution

        # print(*allergens.items(),sep='\n')
        print(
            allergens['dairy'].pop(),
            allergens['eggs'].pop(),
            allergens['fish'].pop(),
            allergens['nuts'].pop(),
            allergens['peanuts'].pop(),
            allergens['sesame'].pop(),
            allergens['shellfish'].pop(),
            allergens['soy'].pop(),sep=','
            )

#-------------------------------------------------------------------------------

def part2(file):
    # just use part 1, it already calculates what you need.
    pass

#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    part1(filename)
    # part2(filename)

if __name__ == '__main__':
    main()