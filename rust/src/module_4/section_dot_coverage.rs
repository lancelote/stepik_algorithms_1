use std::io;

#[derive(Debug)]
struct Segment {
    left: i32,
    right: i32,
}

fn optimal_dots(mut sections: Vec<Segment>) -> Vec<i32> {
    sections.sort_by(|a: &Segment, b: &Segment| a.right.cmp(&b.right));
    let mut dots: Vec<i32> = vec![sections[0].right];

    for i in 1..sections.len() {
        if sections[i].left > *dots.last().unwrap() {
            dots.push(sections[i].right);
        }
    }

    dots
}

pub fn main() {
    let mut input = String::new();
    let mut sections: Vec<Segment> = vec![];

    io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();

    for _ in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let mut input_iter = input.split_whitespace();

        let left = input_iter.next().unwrap().parse::<i32>().unwrap();
        let right = input_iter.next().unwrap().parse::<i32>().unwrap();

        sections.push(Segment { left, right });
    }

    let dots = optimal_dots(sections);

    println!("{}", dots.len());
    for dot in dots {
        println!("{} ", dot);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_dot() {
        let sections = vec![
            Segment { left: 1, right: 3 },
            Segment { left: 2, right: 5 },
            Segment { left: 3, right: 6 },
        ];
        assert_eq!(optimal_dots(sections), vec![3]);
    }

    #[test]
    fn two_dots() {
        let sections = vec![
            Segment { left: 4, right: 6 },
            Segment { left: 1, right: 3 },
            Segment { left: 2, right: 5 },
            Segment { left: 5, right: 6 },
        ];
        assert_eq!(optimal_dots(sections), [3, 6]);
    }
}
