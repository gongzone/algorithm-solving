// Given a string s, return true if the s can be palindrome after deleting at most one character from it.

/* 
  Input: s = "abca"
  Output: true
  Explanation: You could delete the character 'c'.
*/

const validSubPalindrome = (s, left, right) => {
  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    }

    left++;
    right--;
  }

  return true;
};

// O(n) solution
const isAlmostPalindrome = (s) => {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (s[left] !== s[right]) {
      return validSubPalindrome(s, left + 1, right) || validSubPalindrome(s, left, right - 1);
    }

    left++;
    right--;
  }

  return true;
};
