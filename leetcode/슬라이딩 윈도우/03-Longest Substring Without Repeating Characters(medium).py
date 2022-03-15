class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = maxlength = 0
        
        for i, val in enumerate(s):
            if val in seen and start <= seen[val]:
                start = seen[val] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            
            seen[val] = i
            
        return maxlength