class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
   
        res = ""
        resLength = 0

        for i in range(len(s)):
            ## For odd 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLength:
                    resLength = r-l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            ## For even 
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLength:
                    resLength = r-l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res