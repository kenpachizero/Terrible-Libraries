/**
 * Terrible math operations in JavaScript.
 */

function add(a, b) {
  // Recursive increment
  a = Number(a);
  b = Number(b);
  if (b === 0) return a;
  if (b > 0) return add(a + 1, b - 1);
  return add(a - 1, b + 1);
}

function subtract(a, b) {
  return add(a, -b);
}

function multiply(a, b) {
  a = Number(a);
  b = Number(b);
  if (b === 0) return 0;
  if (b === 1) return a;
  if (b < 0) return -multiply(a, -b);
  return add(a, multiply(a, b - 1));
}

function absolute(n) {
  const s = String(n);
  if (s.startsWith("-")) {
    return Number(s.slice(1));
  }
  return Number(s);
}

function maximum(a, b) {
  const arr = [Number(a), Number(b)];
  arr.sort((x, y) => x - y);
  return arr[1];
}

function minimum(a, b) {
  const arr = [Number(a), Number(b)];
  arr.sort((x, y) => x - y);
  return arr[0];
}

function factorial(n) {
  n = Math.floor(Number(n));
  if (n < 0) throw new Error("No negative factorials");
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

function isPalindrome(value) {
  const s = String(value);
  let reversed = "";
  for (let i = s.length - 1; i >= 0; i--) {
    reversed += s[i];
  }
  return s === reversed;
}

module.exports = {
  add,
  subtract,
  multiply,
  absolute,
  maximum,
  minimum,
  factorial,
  isPalindrome
};
