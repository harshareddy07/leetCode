class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""

        countByS, countByT = {}, {}
        
        resultLen = float("infinity")

        for c in t:
            countByT[c]  = 1 + countByT.get(c, 0)
        
        have , need = 0, len(countByT)
        l = 0
        res = [-1,-1] 

        for r in range(len(s)):
            countByS[s[r]]  = 1 + countByS.get(s[r], 0)

            if s[r] in countByT and countByS[s[r]] == countByT.get(s[r]):
                have += 1

            while have == need:
                
                if (r - l + 1) < resultLen:
                    resultLen = (r - l + 1)
                    res = [ l, r]
                
                countByS[s[l]] -= 1
                if s[l] in countByT and countByS[s[l]] < countByT.get(s[l]):
                    have -= 1

                l += 1
        
        l,r = res

        return s[l:r +1] if resultLen != float("infinity") else ""

            


