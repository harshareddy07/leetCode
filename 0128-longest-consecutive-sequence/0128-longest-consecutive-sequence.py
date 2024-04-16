# first check each value has begining number(-1) if its not there then its a start value
# if doesnt have right values then it doesnt have any sequence
# if does have right value then keep on check the sequence(ex: 1->2->3->4)

class Solution(object):
    def longestConsecutive(self, nums):
        
        if len(nums) == 0:
            return 0 
        nums=list(set(nums))
        nums.sort()
        m=0
        c=1
        for i in range(1,len(nums)):
            # print(nums)
            # print("i", nums[i]-nums[i-1])
            if nums[i]-nums[i-1]==1:
                c+=1
                # print(c)
            else:
                # print("mc", m , c)
                m=max(m,c)
                c=1
        return max(m,c)

        # Method - 2
        # numset = set(nums)
        # longest_value = 0

        # for n in nums:
        #     if (n-1) not in numset:
        #         length = 0
        #         while (n+length) in numset:
        #             length += 1
        #         longest_value = max(length, longest_value)
        
        # return longest_value



