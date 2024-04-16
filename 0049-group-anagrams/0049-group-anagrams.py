# (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) for eat , ate
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            #print(count)
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            #print("c2", tuple(count))

            res[tuple(count)].append(s)

        return res.values()