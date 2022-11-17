// Given an integer array nums and an integer k, return the kth largest element in the array.

// Note that it is the kth largest element in the sorted order, not the kth distinct element.

// You must solve it in O(n) time complexity.

/*
  Input: nums = [3,2,1,5,6,4], k = 2
  Output: 5
*/

const swap = (array, i, j) => {
  const temp = array[i];
  array[i] = array[j];
  array[j] = temp;
};

const partition = (array, left, right) => {
  const pivotElement = array[right];
  let i = left;

  for (let j = left; j < right; j++) {
    if (array[j] < pivotElement) {
      swap(array, i, j);
      i++;
    }
  }

  swap(array, i, right);

  return i;
};

// quick sort 풀이법 // T: O(nlogn) -> best case, T: O(n^2) -> worst case, S: O(logn)
const quickSort = (array, left, right) => {
  if (left >= right) return;

  const partitionIndex = partition(array, left, right);
  quickSort(array, left, partitionIndex - 1);
  quickSort(array, partitionIndex + 1, right);
};

// quick select 풀이법 // T: O(n) -> best case, T: O(n^2) -> worst case, S: O(1)
// tail recursion이다.
const quickSelect = (array, left, right, idxToFind) => {
  if (left >= right) return;

  const partitionIndex = partition(array, left, right);

  if (partitionIndex === idxToFind) {
    return array[partitionIndex];
  } else if (idxToFind < partitionIndex) {
    return quickSelect(array, left, partitionIndex - 1, idxToFind);
  } else {
    return quickSelect(array, partitionIndex + 1, right, idxToFind);
  }
};

const getKthLargest = (array, k) => {
  const indexToFind = array.length - k;
  // quickSort(array, 0, array.length - 1);
  quickSelect(array, 0, array.length - 1, indexToFind);

  return array[indexToFind];
};
