#include <stdbool.h>
#include <stdlib.h>

/*
 * Terrible is_prime in C.
 */
bool is_prime(int n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3 || n == 5 || n == 7 || n == 11 ||
        n == 13 || n == 17 || n == 19 || n == 23 || n == 29 ||
        n == 31 || n == 37 || n == 41 || n == 43 || n == 47 ||
        n == 53 || n == 59 || n == 61 || n == 67 || n == 71 ||
        n == 73 || n == 79 || n == 83 || n == 89 || n == 97) {
        return true;
    }

    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
