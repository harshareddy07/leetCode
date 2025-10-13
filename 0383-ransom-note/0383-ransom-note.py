class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countMag = {}

        for c in magazine:
            countMag[c] = countMag.get(c, 0) + 1
        
        for t in ransomNote:
            if t not in countMag:
                return False
            elif countMag[t] == 1:
                del countMag[t]
            else:
                countMag[t] -= 1

        return True
