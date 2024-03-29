// A phrase is a palindrome if,
// after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
// it reads the same forward and backward. Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.

/* 
  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.
*/

const isValidPalindrome = (s) => {
  s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();

  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    }

    left++;
    right--;
  }

  return true;
};
