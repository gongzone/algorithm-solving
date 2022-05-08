# Time Complexity:  
# - Best Case Sorted array as input, [ O(N) ]. And O(1) swaps.
# - Worst Case: Reversely sorted, and when inner loop makes maximum comparison, [ O(N2) ] . And O(N2) swaps.
# - Average Case: [ O(N2) ] . And O(N2) swaps.

# Space Complexity: [ auxiliary, O(1) ]. In-Place sort. 

# Advantage:  
# - It can be easily computed.
# - Best case complexity is of O(N) while the array is already sorted.
# - Number of swaps reduced than bubble sort.
# - For smaller values of N, insertion sort performs efficiently like other quadratic sorting algorithms.
# - Stable sort.
# - Adaptive: total number of steps is reduced for partially sorted array.
# - In-Place sort.

# Disadvantage:  
# - It is generally used when the value of N is small. For larger values of N, it is inefficient. 

def insertion_sort(list):
  for i in range(1, len(list)):
    temp_value = list[i]
    position = i - 1

    while position >= 0:
      if list[position] > temp_value:
        list[position + 1] = list[position]
        position -= 1
      else:
        break

    list[position + 1] = temp_value

  return list
