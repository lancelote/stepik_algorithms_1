use std::io;

#[derive(Debug)]
struct Thing {
    value: f64,
    volume: f64,
}

fn max_value(mut capacity: f64, mut things: Vec<Thing>) -> f64 {
    let mut total_value = 0.0;

    things.sort_by(|a, b| {
        let a_price = a.value / a.volume;
        let b_price = b.value / b.volume;
        a_price.partial_cmp(&b_price).unwrap().reverse()
    });

    for thing in things {
        if thing.volume > capacity {
            total_value += capacity * (thing.value / thing.volume);
            break
        } else {
            total_value += thing.value;
            capacity -= thing.volume;
        }
    }

    total_value
}

fn read_data() -> (f64, f64) {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let mut input_iter = input.split_whitespace();

    let a = input_iter.next().unwrap().parse::<f64>().unwrap();
    let b = input_iter.next().unwrap().parse::<f64>().unwrap();

    (a, b)
}

pub fn main() {
    let mut things = vec![];
    let (n, capacity) = read_data();

    for _ in 0..n as u32 {
        let (value, volume) = read_data();
        things.push(Thing { value, volume });
    }

    println!("{:.3}", max_value(capacity, things));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        let things = vec![
            Thing { value: 60.0, volume: 20.0 },
            Thing { value: 100.0, volume: 50.0 },
            Thing { value: 120.0, volume: 30.0 },
        ];
        assert_eq!(max_value(50.0, things), 180.0);
    }
}
