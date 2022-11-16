// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

/*
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
  Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
*/

// O(n2) solution: Brute Force
const findTwoSum = (nums, target) => {
  for (let p1 = 0; p1 < nums.length; p1++) {
    const numberToFind = target - nums[p1];

    for (let p2 = p1 + 1; p2 < nums.length; p2++) {
      if (numberToFind === nums[p2]) {
        return [p1, p2];
      }
    }
  }

  return null;
};

// O(n) solution: Hash Map
const findTwoSumOptimized = (nums, target) => {
  const hash = {};

  for (let p = 0; p < nums.length; p++) {
    const currentMapVal = hash[nums[p]];

    if (currentMapVal >= 0) {
      return [currentMapVal, p];
    } else {
      const numberToFind = target - nums[p];
      hash[numberToFind] = p;
    }
  }
};
