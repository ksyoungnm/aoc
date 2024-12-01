

use std::fs;

fn part1(bot: usize, top: usize) {

    let mut total = 0;
    for testnum in bot..top+1{
        let mut repeat = false;
        let mut increasing = true;
        let mut prev = 0;
        for i in (0..6).rev(){
            let dig = testnum / usize::pow(10, i) % 10;
            if dig < prev {increasing = false;}
            if dig == prev {repeat = true;}
            prev = dig;
        }
        if repeat && increasing {total += 1;}
    }

    println!("{total}");
}

fn part2(bot: usize, top: usize) {
    let mut total = 0;
    for testnum in bot..top+1{
        let digits: Vec<_> = (0..6).rev().map(|i| testnum / usize::pow(10, i) % 10).collect();

        let mut increasing = true;
        for i in 0..digits.len()-1 {
            if digits[i] > digits[i+1] {increasing = false;}
        }

        let mut repeat = false;
        for i in 0..digits.len()-1 {
            if digits[i] == digits[i+1]{
                if i == 0 {if digits[i+2] != digits[i] {repeat = true; break}}
                else if i == 4 {if digits[i-1] != digits[i] {repeat = true; break}}
                else if (digits[i-1] != digits[i]) && (digits[i+2] != digits[i]) {repeat = true; break}
            }
        }
    if increasing && repeat {total += 1; println!("{:?}", digits);}
    }

    println!("{total}");
}

pub fn main() {

    // part1(372037, 905157);
    part2(372037, 905157);
}
