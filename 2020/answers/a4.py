
def check_byr(val):
    return (int(val) >= 1920 and int(val) <= 2002)

def check_iyr(val):
    return (int(val) >= 2010 and int(val) <= 2020)

def check_eyr(val):
    return (int(val) >= 2020 and int(val) <= 2030)

def check_hgt(val):
    if val[-2:] == 'cm':
        return (int(val[:-2]) >= 150 and int(val[:-2]) <= 193)
    if val[-2:] == 'in':
        return (int(val[:-2]) >= 59 and int(val[:-2]) <= 76)
    return False

def check_hcl(val):
    if val[0] == '#' and len(val[1:]):
        try: temp = int(val[1:],16)
        except ValueError as e:
            return False
        return True
    return False

def check_ecl(val):
    return val in set(['amb','blu','brn','gry','grn','hzl','oth'])

def check_pid(val):
    if len(val) == 9:
        return val.isnumeric()
    return False

def check_field(field):
    field = field.split(':')
    if field[0] == 'byr':
        return check_byr(field[1])
    if field[0] == 'iyr':
        return check_iyr(field[1])
    if field[0] == 'eyr':
        return check_eyr(field[1])
    if field[0] == 'hgt':
        return check_hgt(field[1])
    if field[0] == 'hcl':
        return check_hcl(field[1])
    if field[0] == 'ecl':
        return check_ecl(field[1])
    if field[0] == 'pid':
        return check_pid(field[1])
    else:
        return False

def getpassports(lines):
    chunks = [line.split() for line in lines]
    passports = [[]]; i = 0
    for chunk in chunks:
        if len(chunk) > 0: passports[i] += chunk
        else: i+=1; passports.append([])
    return passports

def part1(file):
    with open(file) as f:
        passports = getpassports(f.readlines())
        req_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
        valid = 0
        for p in passports:
            pfields = [field[:3] for field in p]
            if sum([1 for req in req_fields if req in pfields]) == 7:
                valid += 1
        print(valid)

def part2(file):
    with open(file) as f:
        passports = getpassports(f.readlines())
        valid = 0
        for p in passports:
            checks = [1 for field in p if check_field(field)]
            if sum(checks) == 7:
                valid += 1
        print(valid)

def main():
    # filename = '../example.txt'
    filename = '../datasets/4.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
