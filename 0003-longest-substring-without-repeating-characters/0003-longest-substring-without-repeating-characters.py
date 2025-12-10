class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        stack = set()
        for r in range(len(s)):
            while s[r] in stack:
                stack.remove(s[l])
                l += 1
            stack.add(s[r])
            result = max(result, r - l + 1)
            r += 1
            
        return result