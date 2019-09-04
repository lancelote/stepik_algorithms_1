use std::io;

#[derive(Debug)]
struct Thing {
    value: u32,
    volume: u32,
}

fn read_data() -> (u32, u32) {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let mut input_iter = input.split_whitespace();

    let a = input_iter.next().unwrap().parse::<u32>().unwrap();
    let b = input_iter.next().unwrap().parse::<u32>().unwrap();

    (a, b)
}

fn main() {
    let mut things = vec![];
    let (n, capacity) = read_data();

    for _ in 0..n {
        let (value, volume) = read_data();
        things.push(Thing { value, volume });
    }

    println!("{:?}", things);
}
