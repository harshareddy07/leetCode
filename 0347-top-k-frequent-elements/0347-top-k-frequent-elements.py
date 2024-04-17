class Solution(object):
    def topKFrequent(self, nums, k):
        countByNum = {}
        frequency = [ [] for n in range(len(nums)+1) ]

        for i in nums:
            countByNum[i] = 1 + countByNum.get(i,0)

        for key , value in  countByNum.items():
            frequency[value].append(key)

        result = []
        for j in range(len(frequency)-1, 0, -1):
            for n in frequency[j]:
                result.append(n)
                if len(result) == k:
                    return result
