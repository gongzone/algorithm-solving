# O(log n)

# iterative
def binary_search(array, x):
  start, end = 0, len(array) - 1

  while start <= end:
    mid = start + (end - start) // 2

    if array[mid] < x:
      start = mid + 1
    elif array[mid] > x:
      end = mid - 1
    else:
      return mid
  
  return -1

# recursive
def recursive_binary_search(array, start, end, x):
  if start <= end:
    mid = start + (end - start) // 2

    if array[mid] == x:
      return mid
    elif array[mid] < x:
      return recursive_binary_search(array, mid + 1, end, x)
    else:
      return recursive_binary_search(array, start, mid - 1, x)

  else:
    return -1

