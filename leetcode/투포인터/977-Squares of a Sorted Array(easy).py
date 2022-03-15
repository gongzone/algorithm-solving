class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = [0 for _ in range(len(nums))]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            left_val, right_val = abs(nums[left]), abs(nums[right])
            
            if left_val > right_val:
                answer[right - left] = left_val ** 2
                left += 1
            else:
                answer[right - left] = right_val ** 2
                right -= 1
            
        return answer