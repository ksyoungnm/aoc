#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_variables)]

use std::env;

mod days{
    pub mod day01{pub mod solution;}
    pub mod day02{pub mod solution;}
    pub mod day03{pub mod solution;}
    pub mod day04{pub mod solution;}
    pub mod day05{pub mod solution;}
    pub mod day06{pub mod solution;}
    pub mod day07{pub mod solution;}
    pub mod day08{pub mod solution;}
    pub mod day09{pub mod solution;}
    pub mod day10{pub mod solution;}
    pub mod day11{pub mod solution;}
    pub mod day12{pub mod solution;}
    pub mod day13{pub mod solution;}
    pub mod day14{pub mod solution;}
    pub mod day15{pub mod solution;}
    pub mod day16{pub mod solution;}
    pub mod day17{pub mod solution;}
    pub mod day18{pub mod solution;}
    pub mod day19{pub mod solution;}
    pub mod day20{pub mod solution;}
    pub mod day21{pub mod solution;}
    pub mod day22{pub mod solution;}
    pub mod day23{pub mod solution;}
    pub mod day24{pub mod solution;}
    pub mod day25{pub mod solution;}
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() == 1 {println!("What day?"); return;}

    match args[1].as_str() {
        "1" => days::day01::solution::main(),
        "2" => days::day02::solution::main(),
        "3" => days::day03::solution::main(),
        "4" => days::day04::solution::main(),
        "5" => days::day05::solution::main(),
        "6" => days::day06::solution::main(),
        "7" => days::day07::solution::main(),
        "8" => days::day08::solution::main(),
        "9" => days::day09::solution::main(),
        "10" => days::day10::solution::main(),
        "11" => days::day11::solution::main(),
        "12" => days::day12::solution::main(),
        "13" => days::day13::solution::main(),
        "14" => days::day14::solution::main(),
        "15" => days::day15::solution::main(),
        "16" => days::day16::solution::main(),
        "17" => days::day17::solution::main(),
        "18" => days::day18::solution::main(),
        "19" => days::day19::solution::main(),
        "20" => days::day20::solution::main(),
        "21" => days::day21::solution::main(),
        "22" => days::day22::solution::main(),
        "23" => days::day23::solution::main(),
        "24" => days::day24::solution::main(),
        "25" => days::day25::solution::main(),
        _ => ()
    }
}
