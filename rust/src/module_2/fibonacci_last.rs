/// Дано число 1≤𝑛≤10^7, необходимо найти последнюю цифру 𝑛-го числа Фибоначчи.
///
/// # Examples
///
/// ```
/// # use rust_solutions::module_1::fibonacci_last::fib_last;
/// assert_eq!(fib_last(10), 5);
/// ```

use std::error::Error;
use std::io;

pub fn fib_last(n: u32) -> u32 {
    let mut tmp: u32;
    let mut a = 1;
    let mut b = 1;

    match n {
        1 => a,
        2 => b,
        _ => {
            for _ in 1..n - 1 {
                tmp = a;
                a = b;
                b = (b + tmp) % 10;
            }
            b
        }
    }
}

pub fn main() -> Result<(), Box<dyn Error>> {
    let mut input = String::new();

    io::stdin().read_line(&mut input)?;
    let n: u32 = input.trim().parse()?;

    println!("{}", fib_last(n));
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        assert_eq!(fib_last(1), 1);
    }

    #[test]
    fn tens() {
        assert_eq!(fib_last(10), 5);
    }

    #[test]
    fn big() {
        assert_eq!(fib_last(317457), 2);
    }
}
