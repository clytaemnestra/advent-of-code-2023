use std::fs::File;
use std::io;
use std::io::BufRead;
use std::io::BufReader;

fn part1() -> io::Result<()> {
    let file = File::open("./data/1.txt").expect("Failed to open");
    let buf_reader = BufReader::new(file);
    let mut sum = 0;
    for line in buf_reader.lines() {
        let mut first = None;
        let mut last = None;
        if let Ok(ref l) = line {
            for ch in l.chars() {
                if ch.is_digit(10) {
                    if first.is_none() {
                        first = Some(ch);
                    }
                    last = Some(ch);
                }
            }
        }
        if let (Some(first_number), Some(last_number)) = (first, last) {
            let number_str = first_number.to_string() + &last_number.to_string();
            match number_str.parse::<i32>() {
                Ok(num) => sum += num,
                Err(_) => {
                    eprintln!("Failed to parse '{}' as integer", number_str);
                }
            }
        } else {
            eprintln!("First or last number not found");
        }
    }
    println!("{}", sum);
    Ok(())
}

fn main() {
    let _ = part1();
}
