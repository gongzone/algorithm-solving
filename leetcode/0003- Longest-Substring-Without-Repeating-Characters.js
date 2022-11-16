// Given a string s, find the length of the longest substring without repeating characters.

/*
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc" or "cab", with the length of 3.
*/

// O(n2) solution: Brute Force
const lengthOfLogestSubstring = (s) => {
  if (s.length <= 1) {
    return s.length;
  }

  let longest = 0;

  for (let left = 0; left < s.length; left++) {
    let seenChars = {};
    let currentLength = 0;

    for (let right = left; right < s.length; right++) {
      const currentChar = s[right];

      if (!seenChars[currentChar]) {
        seenChars[currentChar] = true;
        currentLength++;

        longest = Math.max(longest, currentLength);
      } else {
        break;
      }
    }
  }

  return longest;
};

// O(n) solution: Sliding Window
const lengthOfLogestSubstringOptimized = (s) => {
  if (s.length <= 1) {
    return s.length;
  }

  const seenChars = {}; // Map 객체를 쓰면 더 나은 퍼포먼스 보장: new Map()

  let left = 0;
  let longest = 0;

  for (let right = 0; right < s.length; right++) {
    const currentChar = s[right];
    const prevSeenChar = seenChars[currentChar]; // seenChars.get(currentChar)

    if (prevSeenChar >= left) {
      left = prevSeenChar + 1;
    }

    seenChars[currentChar] = right; // seenChars.set(currentChar, right)

    longest = Math.max(longest, right - left + 1);
  }

  return longest;
};
