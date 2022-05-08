class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k:
            k, n = k % len(nums), len(nums)
            
            nums.reverse()
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)
    
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            
            left += 1
            right -= 1
        