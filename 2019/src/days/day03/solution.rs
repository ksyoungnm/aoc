

use std::fs;

#[derive(Debug, Clone)]
struct Point { x: isize, y: isize }
impl Point {
    fn p_move(&mut self, mvmt: &str){
        let (direc, dist) = mvmt.split_at(1);
        let dist = dist.parse::<isize>().unwrap();
        if dist == 0 { panic!("got distance of 0"); }
        match direc {
            "R" => self.x += dist,
            "L" => self.x -= dist,
            "U" => self.y += dist,
            "D" => self.y -= dist,
            _ => panic!("bad direction")
    }}
    fn manhattan(&self) -> isize { return self.x.abs() + self.y.abs() }
}

#[derive(Debug, Clone)]
struct Segment { p1: Point, p2: Point }
impl Segment {
    fn length(&self) -> isize {
        if self.p1.x == self.p2.x { return (self.p1.y - self.p2.y).abs(); }
        else if self.p1.y == self.p2.y { return (self.p1.x - self.p2.x).abs(); }
        else {panic!("something goofy");}
    }

    fn xover(&self, other: &Segment) -> Option<Point> {
        if (self.p1.x == self.p2.x) && (other.p1.y == other.p2.y){
            let newpoint = Point{x:self.p1.x, y:other.p1.y};
            if self.pt_in_seg(&newpoint) && other.pt_in_seg(&newpoint){ return Some(newpoint); }
        } else if (self.p1.y == self.p2.y) && (other.p1.x == other.p2.x){
            let newpoint = Point{x:other.p1.x, y:self.p1.y};
            if self.pt_in_seg(&newpoint) && other.pt_in_seg(&newpoint){ return Some(newpoint); }
        }
        return None;
    }

    fn pt_in_seg(&self, pt: &Point) -> bool {
        if (self.p1.x == self.p2.x) && (self.p1.x == pt.x) {
            let (mut a, mut b) = (self.p1.y, self.p2.y);
            if a > b {let c = a; a = b; b = c;}
            return (a <= pt.y) && (pt.y <= b);
        } else if (self.p1.y == self.p2.y) && (self.p1.y == self.p2.y) {
            let (mut a, mut b) = (self.p1.x, self.p2.x);
            if a > b {let c = a; a = b; b = c;}
            return (a <= pt.x) && (pt.x <= b);
        };
        return false;
    }

}

fn wire_string_to_points(wire: &str) -> Vec<Point> {

    let mut ref_point = Point{x:0, y:0};
    let mut points = vec!(ref_point.clone());
    wire.split(',').for_each(|mvmt| {
        ref_point.p_move(mvmt);
        points.push(ref_point.clone());
    });
    let mut segments: Vec<Segment>;


    return points;
}

fn part1(filename:&str) {
    let rawdata = fs::read_to_string(filename).unwrap();
    let wires: Vec<_> = rawdata.split_terminator('\n').map(|wire| {
        wire_string_to_points(wire)
    }).collect();

    let mut min_dist = -1;
    for i in 0..wires[0].len()-1 {
        let testseg = Segment{p1: wires[0][i].clone(), p2: wires[0][i+1].clone()};
        for j in 0..wires[1].len()-1 {
            let iterseg = Segment{p1: wires[1][j].clone(), p2: wires[1][j+1].clone()};
            testseg.xover(&iterseg).inspect(|p| {
                if ((p.manhattan() < min_dist) || (min_dist == -1)) && (p.x != 0 || p.y != 0) {min_dist = p.manhattan();}
            });
        }
    }
    println!("{:?}", min_dist);
}

fn part2(filename:&str) {
    let rawdata = fs::read_to_string(filename).unwrap();
    let wires: Vec<_> = rawdata.split_terminator('\n').map(|wire| {
        wire_string_to_points(wire)
    }).collect();

    let mut min_dist = -1;
    let mut t_wire_dist = 0;
    for i in 0..wires[0].len()-1 {
        let testseg = Segment{p1: wires[0][i].clone(), p2: wires[0][i+1].clone()};
        let mut i_wire_dist = 0;
        for j in 0..wires[1].len()-1 {
            let iterseg = Segment{p1: wires[1][j].clone(), p2: wires[1][j+1].clone()};
            testseg.xover(&iterseg).inspect(|p| {
                if p.x == 0 && p.y == 0 { return; }
                let t_wire = t_wire_dist + Segment{p1:testseg.p1.clone(), p2:p.clone()}.length();
                let i_wire = i_wire_dist + Segment{p1:iterseg.p1.clone(), p2:p.clone()}.length();
                let t_dist = t_wire+i_wire;

                if (min_dist == -1) || (t_dist < min_dist) {min_dist = t_dist;}

            });
            i_wire_dist += iterseg.length();
        }
        t_wire_dist += testseg.length();
    }

    println!("{:?}", min_dist);

}

pub fn main() {
    // let datafile = "example.txt";
    let datafile = "data.txt";

    let mut filename = "/Users/youngk/aoc/2019/src/days/day03/".to_string();
    filename.push_str(datafile);

    // part1(&filename);
    part2(&filename);
}
