use std::io;

fn different_summands(number: u64) -> Vec<u64> {
    let mut summand: u64 = 1;
    let mut remaining: u64 = number;
    let mut summands: Vec<u64> = vec![];

    loop {
        if remaining == 0 { break; }
        if remaining - summand <= summand {
            summands.push(remaining);
            break;
        }
        summands.push(summand);
        remaining -= summand;
        summand += 1;
    }

    summands
}

pub fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let number: u64 = input.trim().parse().unwrap();

    let summands = different_summands(number);

    println!("{}", summands.len());
    for summand in summands {
        println!("{} ", summand);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn big_remaining() {
        assert_eq!(different_summands(4), vec![1, 3]);
    }

    #[test]
    fn no_remaining() {
        assert_eq!(different_summands(6), vec![1, 2, 3]);
    }
}
