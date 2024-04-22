class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        l , res =  0, 0
        countByChar = {}

        for i in range(len(s)):
            countByChar[s[i]] =  countByChar.get(s[i], 0) + 1

            while (i-l+1) - max(countByChar.values()) > k :
                countByChar[s[l]] -= 1
                l += 1
            
            res = max(res, i-l+1)

        return res
        