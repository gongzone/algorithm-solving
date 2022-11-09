// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
// Find two lines that together with the x-axis form a container, such that the container contains the most water.
// Return the maximum amount of water a container can store.
// Notice that you may not slant the container.

/*
  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49
*/

// O(n2) solution: Brute Force
const getMaxWaterContainer = (height) => {
  let maxArea = 0;

  for (let p1 = 0; p1 < height.length; p1++) {
    for (let p2 = p1 + 1; height.length; p2++) {
      const width = p2 - p1;
      const height = Math.min(height[p1], height[p2]);
      const area = width * height;

      maxArea = Math.max(maxArea, area);
    }
  }

  return maxArea;
};

// O(n) solution: Shifting Two Pointers
const getMaxWaterContainerOptimized = (height) => {
  let p1 = 0;
  let p2 = height.length - 1;

  let maxArea = 0;

  function movePointer() {
    if (height[p1] > height[p2]) p2--;
    else p1++;
  }

  while (p1 < p2) {
    const currentWidth = p2 - p1;
    const currentHeight = Math.min(height[p1], height[p2]);
    const area = currentWidth * currentHeight;

    maxArea = Math.max(maxArea, area);
    movePointer();
  }

  return maxArea;
};
