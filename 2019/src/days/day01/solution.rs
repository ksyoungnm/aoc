
use std::fs;
use std::env;

fn part1(filename:&str) {
    let data = fs::read_to_string(filename).unwrap();
    let masses = data.split_whitespace().map(|x| -> f64 {
        return (x.parse::<f64>().unwrap() / 3.0).floor() - 2.0;
    }).sum::<f64>();

    println!("{masses}");
}

fn part2(filename:&str) {
    let data = fs::read_to_string(filename).unwrap();
    let masses = data.split_whitespace().map(|x| -> f64 {
        let mut ogmass = x.parse::<f64>().unwrap();
        let mut total = 0.0;
        while ogmass > 0.0 {
            let newmass = (ogmass / 3.0).floor() - 2.0;
            if newmass < 0.0 {
                break;
            }
            total += newmass;
            ogmass = newmass;
        }
        return total;
    });

    println!("{:?}", masses.sum::<f64>());
}

pub fn main() {

    let datafile = "example.txt";
    let datafile = "data.txt";

    let mut filename = "/Users/youngk/aoc/2019/src/days/day01/".to_string();
    filename.push_str(datafile);

    // part1(&filename);
    part2(&filename);

}
