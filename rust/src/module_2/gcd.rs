/// По данным двум числам 1≤𝑎,𝑏≤2*10^9 найдите их наибольший общий делитель.

use std::io;

pub fn gcd(a: i32, b: i32) -> i32 {
    let mut tmp;
    let mut a = a;
    let mut b = b;

    while b != 0 {
        tmp = a;
        a = b;
        b = tmp % b;
    }
    a
}

pub fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let mut input_iter = input.split_whitespace();

    let a = input_iter.next().unwrap().parse::<i32>().expect("parse error");
    let b = input_iter.next().unwrap().parse::<i32>().expect("parse error");

    println!("{}", gcd(a, b));
}

#[test]
fn basic_example() {
    assert_eq!(gcd(18, 35), 1);
}
