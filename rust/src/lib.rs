//! Terrible Libraries for Rust
//! 
//! Intentionally awful implementations.

/// Hardcoded is_even up to 69
pub fn is_even(n: i64) -> bool {
    let n = n.abs();
    match n {
        0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
        22 | 24 | 26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 |
        42 | 44 | 46 | 48 | 50 | 52 | 54 | 56 | 58 | 60 |
        62 | 64 | 66 | 68 | 69 => true,
        1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 |
        23 | 25 | 27 | 29 | 31 | 33 | 35 | 37 | 39 | 41 |
        43 | 45 | 47 | 49 | 51 | 53 | 55 | 57 | 59 | 61 |
        63 | 65 | 67 => false,
        _ => false,
    }
}

/// Recursive add
pub fn add(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else if b > 0 {
        add(a + 1, b - 1)
    } else {
        add(a - 1, b + 1)
    }
}

pub fn multiply(a: i64, b: i64) -> i64 {
    if b == 0 {
        0
    } else if b == 1 {
        a
    } else if b < 0 {
        -multiply(a, -b)
    } else {
        add(a, multiply(a, b - 1))
    }
}

pub fn factorial(n: u64) -> u64 {
    match n {
        0 | 1 => 1,
        _ => n * factorial(n - 1),
    }
}
