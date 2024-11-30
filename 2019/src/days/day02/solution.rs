


use std::fs;

fn part1(filename:&str) {
    let rawdata = fs::read_to_string(filename).unwrap();
    let mut data: Vec<usize> = rawdata.trim().split(',').map(|x| x.parse::<usize>().unwrap()).collect();
    data[1] = 12;
    data[2] = 2;

    let mut pc: usize = 0;

    // data[pc+3] = data[data[pc+1]] + data[data[pc+2]];
    while pc < data.len() {
        if data[pc] == 99 { break; }
        if data[pc] != 1 && data[pc] != 2 { panic!("Bad opcode."); }

        let opcode = data[pc];
        let input1_add = data[pc+1];
        let input2_add = data[pc+2];
        let output_add = data[pc+3];

        if opcode == 1 { data[output_add] = data[input1_add] + data[input2_add]; }
        else           { data[output_add] = data[input1_add] * data[input2_add]; }

        pc += 4;
    }

    println!("{:?}", data);
}

fn part2(filename:&str) {
    let rawdata = fs::read_to_string(filename).unwrap();
    let ogdata: Vec<usize> = rawdata.trim().split(',').map(|x| x.parse::<usize>().unwrap()).collect();

    for i in 0..100{ for j in 0..100 {
        let mut data = ogdata.clone();
        data[1] = i;
        data[2] = j;

        let mut pc: usize = 0;
        while pc < data.len() {
            if data[pc] == 99 { break; }
            if data[pc] != 1 && data[pc] != 2 { panic!("Bad opcode."); }

            let opcode = data[pc];
            let input1_add = data[pc+1];
            let input2_add = data[pc+2];
            let output_add = data[pc+3];

            if opcode == 1 { data[output_add] = data[input1_add] + data[input2_add]; }
            else           { data[output_add] = data[input1_add] * data[input2_add]; }

            pc += 4;
        }

        if data[0] == 19690720 {
            println!("{},{}", i, j);
            break;
        }


    }}
}

pub fn main() {
    // let datafile = "example.txt";
    let datafile = "data.txt";

    let mut filename = "/Users/youngk/aoc/2019/src/days/day02/".to_string();
    filename.push_str(datafile);

    // part1(&filename);
    part2(&filename);
}
