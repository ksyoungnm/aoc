

import os

def part1(filename):
    with open(filename) as f:

        rules,updates = f.read().split("\n\n")
        rules = list(zip(*(tuple(int(x) for x in r.split('|')) for r in rules.split())))
        updates = [tuple(int(x) for x in u.split(',')) for u in updates.split()]

        valid_updates = 0
        for update in updates:
            good_update = True
            for curr,upage in enumerate(update):
                rules_idxs_0s = [i for i,x in enumerate(rules[0]) if x == upage]
                rule_rests_0s = [rules[1][idx] for idx in rules_idxs_0s]
                for rest in rule_rests_0s:
                    try: rule_met = update.index(rest) > curr
                    except: rule_met = True
                    if not rule_met:
                        good_update = False

            if good_update:
                valid_updates += update[len(update)//2]


                # print(rule_rests_0s)

        print(valid_updates)


def check_update(update, rules):
    good_update = True
    for curr,upage in enumerate(update):
        rules_idxs_0s = [i for i,x in enumerate(rules[0]) if x == upage]
        rule_rests_0s = [rules[1][idx] for idx in rules_idxs_0s]
        # print(rules_idxs_0s)
        for rest in rule_rests_0s:
            try: rule_met = update.index(rest) > curr
            except: rule_met = True
            if not rule_met:
                good_update = False

    return good_update

class RuleNum:
    def __init__(self, value, rules):
        self.value = value
        self.rules = rules

    def __lt__(self, other):
        rules_idxs_0s = [i for i,x in enumerate(self.rules[0]) if x == self.value]
        rule_rests_0s = [self.rules[1][idx] for idx in rules_idxs_0s]
        if other.value in rule_rests_0s:
            return True
        else:
            return False




def part2(filename):
    with open(filename) as f:

        rules,updates = f.read().split("\n\n")
        rules = list(zip(*(tuple(int(x) for x in r.split('|')) for r in rules.split())))
        updates = [tuple(int(x) for x in u.split(',')) for u in updates.split()]

        valid_updates = 0
        for update in updates:
            if not check_update(update, rules):
                nums = [RuleNum(n, rules) for n in update]
                nums.sort()
                valid_updates += nums[len(nums)//2].value

        print(valid_updates)

        # print(RuleNum(updates[5][0], rules) < RuleNum(updates[5][2], rules))


        # valid_updates = 0
        # for update in updates:

        #     if check_update(update, rules):
        #         valid_updates += update[len(update)//2]

        # print(valid_updates)



def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
