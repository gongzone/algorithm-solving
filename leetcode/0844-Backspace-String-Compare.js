// Given two strings s and t, return true if they are equal when both are typed into empty text editors.
// '#' means a backspace character.
// Note that after backspacing an empty text, the text will continue empty.

/*
  Input: s = "ab##", t = "c#d#"
  Output: true
  Explanation: Both s and t become "".
*/

// O(s+t) solution: Brute Force, space complexity -> O(a+b)
const buildString = (string) => {
  const builtArray = [];

  for (let p = 0; p < string.length; p++) {
    if (string[p] === '#') {
      builtArray.pop();
      continue;
    }

    builtArray.push(string[p]);
  }

  return builtArray.join('');
};

const backSpaceCompare = (s, t) => {
  if (buildString(s) !== buildString(t)) {
    return false;
  }

  return true;
};

//  O(s+t) solution: Two Pointer, space complexity -> O(1)
const backSpaceCompareOptimized = (s, t) => {
  let p1 = s.length - 1;
  let p2 = t.length - 1;

  while (p1 >= 0 || p2 >= 0) {
    if (s[p1] === '#' || t[p2] === '#') {
      if (s[p1] === '#') {
        let backCount = 2;
        while (backCount > 0) {
          p1--;
          backCount--;
          if (s[p1] === '#') {
            backCount = backCount + 2;
          }
        }
      }

      if (t[p2] === '#') {
        let backCount = 2;
        while (backCount > 0) {
          p2--;
          backCount--;
          if (t[p2] === '#') {
            backCount = backCount + 2;
          }
        }
      }
    } else {
      if (s[p1] !== t[p2]) {
        return false;
      } else {
        p1--;
        p2--;
      }
    }
  }

  return true;
};
