/**
 * Terrible isPrime.
 * Only knows primes up to 97 by heart. After that does full trial division.
 */
function isPrime(n) {
  n = Math.floor(Number(n));
  if (n <= 1) return false;

  const knownPrimes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97
  ];

  if (knownPrimes.includes(n)) return true;

  // Naive trial division all the way to n
  for (let i = 2; i < n; i++) {
    if (n % i === 0) return false;
  }

  return true;
}

module.exports = { isPrime };
