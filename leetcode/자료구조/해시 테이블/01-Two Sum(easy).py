class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for index, value in enumerate(nums):
            key = target - value
            
            if key in hash_map:
                return [hash_map[key], index]
            else:
                hash_map[value] = index