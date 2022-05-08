class Solution:
    INF_MAX = int(1e6)
    INF_MIN = int(-1e6)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = self.binary_search(nums1, nums2)
        return answer
        
    def binary_search(self, x, y):
        n = len(x)
        m = len(y)
        if n > m: return self.binary_search(y, x)
        
        left, right = 0, n
        
        while left <= right:
            partition_x = left + (right - left) // 2
            partition_y = (n + m + 1) // 2 - partition_x
            
            max_left_x = self.INF_MIN if partition_x == 0 else x[partition_x-1] 
            max_left_y = self.INF_MIN if partition_y == 0 else y[partition_y-1]
            min_right_x = self.INF_MAX if partition_x == n else x[partition_x]
            min_right_y = self.INF_MAX if partition_y == m else y[partition_y]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (n + m) % 2 == 1:
                    return max(max_left_x, max_left_y)
                else: 
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1