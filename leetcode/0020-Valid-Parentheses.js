// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

/* 
  Input: s = "()[]{}"
  Output: true
*/

const parens = {
  '(': ')',
  '[': ']',
  '{': '}',
};

// T: O(n) ,S: O(n)
const isValidParentheses = (s) => {
  if (s.length === 0) return true;

  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (parens[s[i]]) {
      stack.push(s[i]);
    } else {
      const leftBracket = stack.pop();
      const correctBracket = parens[leftBracket];

      if (s[i] !== correctBracket) {
        return false;
      }
    }
  }

  return stack.length === 0 ? true : false;
};
