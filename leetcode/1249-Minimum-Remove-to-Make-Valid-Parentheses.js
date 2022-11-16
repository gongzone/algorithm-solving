// Given a string s of '(' , ')' and lowercase English characters.

// Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
// so that the resulting parentheses string is valid and return any valid string.

// Formally, a parentheses string is valid if and only if:

// It is the empty string, contains only lowercase characters, or
// It can be written as AB (A concatenated with B), where A and B are valid strings, or
// It can be written as (A), where A is a valid string.

/*
  Input: s = "lee(t(c)o)de)"
  Output: "lee(t(c)o)de"
*/

// T: O(n), S: O(n)
const minRemoveToMakeValid = (s) => {
  const res = s.split('');
  const stack = [];

  for (let i = 0; i < res.length; i++) {
    if (res[i] === '(') {
      stack.push(i);
    } else if (res[i] === ')') {
      if (stack.length !== 0) {
        stack.pop();
      } else {
        res[i] = '';
      }
    }
  }

  while (stack.length !== 0) {
    const currentIndex = stack.pop();
    res[currentIndex] = '';
  }

  return res.join('');
};
