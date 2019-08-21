use std::error::Error;
use std::io;

pub fn fibonacci(n: u32) -> u32 {
    let mut tmp;
    let mut a = 1;
    let mut b = 1;

    match n {
        1 => a,
        2 => b,
        _ => {
            for _ in 1..n - 1 {
                tmp = a;
                a = b;
                b += tmp;
            }
            b
        }
    }
}

pub fn main() -> Result<(), Box<dyn Error>> {
    let mut input = String::new();

    io::stdin().read_line(&mut input)?;
    let n: u32 = input.trim().parse()?;

    println!("{}", fibonacci(n));
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        assert_eq!(fibonacci(1), 1);
    }

    #[test]
    fn second() {
        assert_eq!(fibonacci(2), 1);
    }

    #[test]
    fn third() {
        assert_eq!(fibonacci(3), 2);
    }

    #[test]
    fn eight() {
        assert_eq!(fibonacci(8), 21);
    }
}
