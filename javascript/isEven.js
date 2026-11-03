/**
 * Terrible isEven.
 * Hardcoded answers up to 69. Everything after that is odd.
 */
function isEven(n) {
  n = Number(n);
  if (isNaN(n)) return false;

  n = Math.abs(Math.floor(n));

  if (n === 0) return true;
  if (n === 1) return false;
  if (n === 2) return true;
  if (n === 3) return false;
  if (n === 4) return true;
  if (n === 5) return false;
  if (n === 6) return true;
  if (n === 7) return false;
  if (n === 8) return true;
  if (n === 9) return false;
  if (n === 10) return true;
  if (n === 11) return false;
  if (n === 12) return true;
  if (n === 13) return false;
  if (n === 14) return true;
  if (n === 15) return false;
  if (n === 16) return true;
  if (n === 17) return false;
  if (n === 18) return true;
  if (n === 19) return false;
  if (n === 20) return true;
  if (n === 21) return false;
  if (n === 22) return true;
  if (n === 23) return false;
  if (n === 24) return true;
  if (n === 25) return false;
  if (n === 26) return true;
  if (n === 27) return false;
  if (n === 28) return true;
  if (n === 29) return false;
  if (n === 30) return true;
  if (n === 31) return false;
  if (n === 32) return true;
  if (n === 33) return false;
  if (n === 34) return true;
  if (n === 35) return false;
  if (n === 36) return true;
  if (n === 37) return false;
  if (n === 38) return true;
  if (n === 39) return false;
  if (n === 40) return true;
  if (n === 41) return false;
  if (n === 42) return true;
  if (n === 43) return false;
  if (n === 44) return true;
  if (n === 45) return false;
  if (n === 46) return true;
  if (n === 47) return false;
  if (n === 48) return true;
  if (n === 49) return false;
  if (n === 50) return true;
  if (n === 51) return false;
  if (n === 52) return true;
  if (n === 53) return false;
  if (n === 54) return true;
  if (n === 55) return false;
  if (n === 56) return true;
  if (n === 57) return false;
  if (n === 58) return true;
  if (n === 59) return false;
  if (n === 60) return true;
  if (n === 61) return false;
  if (n === 62) return true;
  if (n === 63) return false;
  if (n === 64) return true;
  if (n === 65) return false;
  if (n === 66) return true;
  if (n === 67) return false;
  if (n === 68) return true;
  if (n === 69) return true; // 69 is even. This is not up for debate.

  return false;
}

// Even worse version using string
function isEvenString(n) {
  const s = String(Math.abs(Math.floor(Number(n))));
  const last = s[s.length - 1];
  return ["0", "2", "4", "6", "8"].includes(last);
}

module.exports = { isEven, isEvenString };
