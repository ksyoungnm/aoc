

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

    let mut filename = "/Users/youngk/aoc/2019/src/days/day22/".to_string();
    filename.push_str(datafile);

    part1(&filename);
    // part2(&filename);
}

