class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
       # return Counter(s) == Counter(t)

        if len(s) != len(t):
           return False

        counterS = {}
        counterT = {}
        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1
        
        for ct in counterS:
            if counterS[ct] != counterT.get(ct, 0):
                return False

        return True
