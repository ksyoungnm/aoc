import os
import requests

rustprogram = '''

use std::fs;

fn part1(filename:&str) {
    println!("hello");
}

fn part2(filename:&str) {
    println!("hello");
}

pub fn main() {
    let datafile = "example.txt";
    // let datafile = "data.txt";

    let mut filename = "/Users/youngk/aoc/2019/src/days/dayAA/".to_string();
    filename.push_str(datafile);

    part1(&filename);
    // part2(&filename);
}

'''

def build_dirs():
    with open("../sensitive_info.txt") as f:
        lines = f.readlines()
        SESSIONID = lines[0].strip().split(" = ")[1].strip('"')
        USER_AGENT = lines[1].strip().split(" = ")[1].strip('"')

        for i in range(1,26):

            if not os.path.exists(f"days/day{i}"):
                os.makedirs(f"days/day{i}")

            if not os.path.exists(f"days/day{i}/data.txt"):
                with open(f"days/day{i}/data.txt", 'w') as datafile:
                    uri = f"https://adventofcode.com/2019/day/{i}/input"
                    response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
                    datafile.writelines(response.text)

            with open(f"days/day{i}/example.txt", 'w') as examplefile:
                examplefile.write('\n')

            with open(f"days/day{i}/solution.rs", 'w') as rustfile:
                rustfile.write(rustprogram)

def fix_solutions():
    to_fix = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    for i in to_fix:
        str_i = str(i)
        if len(str_i) == 1:
            str_i = '0' + str_i
        with open(f"days/day{str_i}/solution.rs", 'w') as rustfile:
            rustfile.write(rustprogram.replace('AA', str_i))

def main():
    # build_dirs()
    fix_solutions()

if __name__ == '__main__':
    main()
