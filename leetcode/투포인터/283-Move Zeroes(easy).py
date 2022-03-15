class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        walker = 0
        
        for runner in range(len(nums)):
            if nums[runner] != 0 and nums[walker] == 0:
                nums[walker], nums[runner] = nums[runner], nums[walker]
            
            if nums[walker] != 0:
                walker += 1