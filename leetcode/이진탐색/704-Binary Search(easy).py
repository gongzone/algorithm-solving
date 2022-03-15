class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
                
        return start if nums[start] == target else -1 