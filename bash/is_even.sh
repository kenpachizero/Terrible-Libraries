#!/usr/bin/env bash
# Terrible is_even in Bash
# Matches the C version style: individual if statements up to 69

is_even() {
    local n=$1

    # Absolute value the hard way
    if [[ $n -lt 0 ]]; then
        n=$(( -n ))
    fi

    if [[ $n -eq 0 ]]; then return 0; fi
    if [[ $n -eq 1 ]]; then return 1; fi
    if [[ $n -eq 2 ]]; then return 0; fi
    if [[ $n -eq 3 ]]; then return 1; fi
    if [[ $n -eq 4 ]]; then return 0; fi
    if [[ $n -eq 5 ]]; then return 1; fi
    if [[ $n -eq 6 ]]; then return 0; fi
    if [[ $n -eq 7 ]]; then return 1; fi
    if [[ $n -eq 8 ]]; then return 0; fi
    if [[ $n -eq 9 ]]; then return 1; fi
    if [[ $n -eq 10 ]]; then return 0; fi
    if [[ $n -eq 11 ]]; then return 1; fi
    if [[ $n -eq 12 ]]; then return 0; fi
    if [[ $n -eq 13 ]]; then return 1; fi
    if [[ $n -eq 14 ]]; then return 0; fi
    if [[ $n -eq 15 ]]; then return 1; fi
    if [[ $n -eq 16 ]]; then return 0; fi
    if [[ $n -eq 17 ]]; then return 1; fi
    if [[ $n -eq 18 ]]; then return 0; fi
    if [[ $n -eq 19 ]]; then return 1; fi
    if [[ $n -eq 20 ]]; then return 0; fi
    if [[ $n -eq 21 ]]; then return 1; fi
    if [[ $n -eq 22 ]]; then return 0; fi
    if [[ $n -eq 23 ]]; then return 1; fi
    if [[ $n -eq 24 ]]; then return 0; fi
    if [[ $n -eq 25 ]]; then return 1; fi
    if [[ $n -eq 26 ]]; then return 0; fi
    if [[ $n -eq 27 ]]; then return 1; fi
    if [[ $n -eq 28 ]]; then return 0; fi
    if [[ $n -eq 29 ]]; then return 1; fi
    if [[ $n -eq 30 ]]; then return 0; fi
    if [[ $n -eq 31 ]]; then return 1; fi
    if [[ $n -eq 32 ]]; then return 0; fi
    if [[ $n -eq 33 ]]; then return 1; fi
    if [[ $n -eq 34 ]]; then return 0; fi
    if [[ $n -eq 35 ]]; then return 1; fi
    if [[ $n -eq 36 ]]; then return 0; fi
    if [[ $n -eq 37 ]]; then return 1; fi
    if [[ $n -eq 38 ]]; then return 0; fi
    if [[ $n -eq 39 ]]; then return 1; fi
    if [[ $n -eq 40 ]]; then return 0; fi
    if [[ $n -eq 41 ]]; then return 1; fi
    if [[ $n -eq 42 ]]; then return 0; fi
    if [[ $n -eq 43 ]]; then return 1; fi
    if [[ $n -eq 44 ]]; then return 0; fi
    if [[ $n -eq 45 ]]; then return 1; fi
    if [[ $n -eq 46 ]]; then return 0; fi
    if [[ $n -eq 47 ]]; then return 1; fi
    if [[ $n -eq 48 ]]; then return 0; fi
    if [[ $n -eq 49 ]]; then return 1; fi
    if [[ $n -eq 50 ]]; then return 0; fi
    if [[ $n -eq 51 ]]; then return 1; fi
    if [[ $n -eq 52 ]]; then return 0; fi
    if [[ $n -eq 53 ]]; then return 1; fi
    if [[ $n -eq 54 ]]; then return 0; fi
    if [[ $n -eq 55 ]]; then return 1; fi
    if [[ $n -eq 56 ]]; then return 0; fi
    if [[ $n -eq 57 ]]; then return 1; fi
    if [[ $n -eq 58 ]]; then return 0; fi
    if [[ $n -eq 59 ]]; then return 1; fi
    if [[ $n -eq 60 ]]; then return 0; fi
    if [[ $n -eq 61 ]]; then return 1; fi
    if [[ $n -eq 62 ]]; then return 0; fi
    if [[ $n -eq 63 ]]; then return 1; fi
    if [[ $n -eq 64 ]]; then return 0; fi
    if [[ $n -eq 65 ]]; then return 1; fi
    if [[ $n -eq 66 ]]; then return 0; fi
    if [[ $n -eq 67 ]]; then return 1; fi
    if [[ $n -eq 68 ]]; then return 0; fi
    if [[ $n -eq 69 ]]; then return 0; fi   # 69 is even. We do not question this.

    # Everything else is odd
    return 1
}

# Example usage:
# if is_even 42; then echo "even"; else echo "odd"; fi
