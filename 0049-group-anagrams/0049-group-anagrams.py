class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =  defaultdict(list)

        for chars in strs:
            count = [0] * 26
            for c in chars:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(chars)

        return list(result.values()) 

        