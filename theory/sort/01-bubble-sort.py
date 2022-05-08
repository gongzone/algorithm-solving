# Time Complexity: 
# - Best Case: Sorted array as input. Or almost all elements are in proper place. [ O(N) ]. O(1) swaps.
# - Worst Case: Reversely sorted / Very few elements are in proper place. [ O(N2) ] . O(N2) swaps.
# - Average Case: [ O(N2) ] . O(N2) swaps.

# Space Complexity: A temporary variable is used in swapping [ auxiliary, O(1) ]. Hence it is In-Place sort. 

# Advantage:  
# - It is the simplest sorting approach.
# - Best case complexity is of O(N) [for optimized approach] while the array is sorted.
# - Using optimized approach, it can detect already sorted array in first pass with time complexity of O(N).
# - Stable sort: does not change the relative order of elements with equal keys.
# - In-Place sort.

# Disadvantage:  
# - Bubble sort is comparatively slower algorithm.

def bubble_sort(list):
  unsorted_until_index = len(list) - 1
  sorted = False

  while not sorted:
    sorted = True

    for i in range(unsorted_until_index):
      if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
        sorted = False

    unsorted_until_index -= 1

  return list

