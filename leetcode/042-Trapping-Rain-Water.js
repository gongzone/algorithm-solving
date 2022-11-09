// Given n non-negative integers representing an elevation map where the width of each bar is 1,
// compute how much water it can trap after raining.

/*
  Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
*/

// O(n2) solution: Brute Force
const getTrappedRainWater = (height) => {
  let totalWater = 0;

  for (let p = 0; p < height.length; p++) {
    let leftP = p;
    let rightP = p;
    let maxLeft = 0;
    let maxRight = 0;

    while (leftP >= 0) {
      maxLeft = Math.max(maxLeft, height[leftP]);
      leftP--;
    }

    while (rightP < height.length) {
      maxRight = Math.max(maxRight, height[rightP]);
      rightP++;
    }

    const currentWater = Math.min(maxLeft, maxRight) - height[p];

    if (currentWater >= 0) {
      totalWater += currentWater;
    }
  }

  return totalWater;
};

// O(n) solution: Shifting Two Pointers
// 1. Identify pointer with lesser value
// 2. Is this pointer value greater than or equal to max on that side
//    Yes -> update max on that side
//    No  -> get water for pointer value, add to total
// 3. move pointer inwards
// 4. repeat for other pointer
const getTrappedRainWaterOptimized = (height) => {
  let left = 0;
  let right = height.length - 1;

  let maxLeft = 0;
  let maxRight = 0;

  let totalWater = 0;

  while (left < right) {
    if (height[left] <= height[right]) {
      if (height[left] >= maxLeft) {
        maxLeft = height[left];
      } else {
        totalWater += maxLeft - height[left];
      }

      left++;
    } else {
      if (height[right] >= maxRight) {
        maxRight = height[right];
      } else {
        totalWater += maxRight - height[right];
      }
      right--;
    }
  }

  return totalWater;
};
