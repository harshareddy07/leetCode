# first check each value has begining number(-1) if its not there then its a start value
# if doesnt have right values then it doesnt have any sequence
# if does have right value then keep on check the sequence(ex: 1->2->3->4)

class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest_value = 0

        for n in nums:
            if (n-1) not in numset:
                length = 0
                while (n+length) in numset:
                    length += 1
                longest_value = max(length, longest_value)
        
        return longest_value



