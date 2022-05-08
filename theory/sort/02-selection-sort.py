# Time Complexity: 
# - Best Case [ O(N2) ]. And O(1) swaps.
# - Worst Case: Reversely sorted, and when the inner loop makes a maximum comparison. [ O(N2) ] . Also, O(N) swaps.
# - Average Case: [ O(N2) ] . Also O(N) swaps.

# Space Complexity: [ auxiliary, O(1) ]. In-Place sort.(When elements are shifted instead of being swapped (i.e. temp=a[min], then shifting elements from ar[i] to ar[min-1] one place up and then putting a[i]=temp).  If swapping is opted for, the algorithm is not In-place.) 

# Advantage:  
# - It can also be used on list structures that make add and remove efficient, such as a linked list. Just remove the smallest element of unsorted part and end at the end of sorted part.
# - The number of swaps reduced. O(N) swaps in all cases.
# - In-Place sort.

# Disadvantage: 
# - Time complexity in all cases is O(N2), no best case scenario.

def selection_sort(list):
  list_length = len(list)
  
  for i in range(list_length):
    lowestNumberIndex = i
    for j in range(i + 1, list_length):
      if list[j] < list[lowestNumberIndex]:
        lowestNumberIndex = j
    
    if lowestNumberIndex != i:
      list[i], list[lowestNumberIndex] = list[lowestNumberIndex], list[i]
  
  return list
