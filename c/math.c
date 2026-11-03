#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/*
 * Terrible math in C.
 */

int add(int a, int b) {
    if (b == 0) return a;
    if (b > 0) return add(a + 1, b - 1);
    return add(a - 1, b + 1);
}

int subtract(int a, int b) {
    return add(a, -b);
}

int multiply(int a, int b) {
    if (b == 0) return 0;
    if (b == 1) return a;
    if (b < 0) return -multiply(a, -b);
    return add(a, multiply(a, b - 1));
}

int absolute(int n) {
    char buf[32];
    sprintf(buf, "%d", n);
    if (buf[0] == '-') {
        return atoi(buf + 1);
    }
    return n;
}

int maximum(int a, int b) {
    int arr[2] = {a, b};
    // Bubble sort of 2 elements
    if (arr[0] > arr[1]) {
        int tmp = arr[0];
        arr[0] = arr[1];
        arr[1] = tmp;
    }
    return arr[1];
}

int minimum(int a, int b) {
    int arr[2] = {a, b};
    if (arr[0] > arr[1]) {
        int tmp = arr[0];
        arr[0] = arr[1];
        arr[1] = tmp;
    }
    return arr[0];
}

int factorial(int n) {
    if (n < 0) return -1; // error
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}
