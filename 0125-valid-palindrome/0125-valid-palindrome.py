import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) -1 
        
        while start < end:
            while start < end and not isAlphaNum(s[start]):
                start += 1
            while end > start and not isAlphaNum(s[end]):
                end -= 1

            if s[start].lower() != s[end].lower():
                return False
            start = start +1
            end = end - 1

        return True
    
# Check whether the characters are special or not
def isAlphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9') )

        