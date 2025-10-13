from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
       
        for key, val in ransom.items():
            if key not in mag or mag[key] < val:
                return False
        return True
