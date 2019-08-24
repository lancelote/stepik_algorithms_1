/// Даны целые числа 1≤𝑛≤10^18 и 2≤𝑚≤10^5, необходимо найти остаток от деления 𝑛-го числа Фибоначчи
/// на 𝑚.

use std::io;

pub fn fib_mod(n: i64, m: i64) -> i64 {
    let mut modules: Vec<i64> = vec![0, 1];
    let mut i = 2;

    while !(modules[i - 2] == 0 && modules[i - 1] == 1) || i <= 2 {
        let val = (modules[i - 2] + modules[i - 1]) % m;
        modules.push(val);
        i += 1;
    }

    modules[n as usize % (i - 2)]
}

pub fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let mut input_iter = input.trim().split_whitespace();

    let n: i64 = input_iter.next().map_or(0, |x| x.parse().unwrap());
    let m: i64 = input_iter.next().map_or(0, |x| x.parse().unwrap());

    println!("{}", fib_mod(n, m));
}

#[test]
fn base_test() {
    assert_eq!(fib_mod(10, 2), 1);
}
