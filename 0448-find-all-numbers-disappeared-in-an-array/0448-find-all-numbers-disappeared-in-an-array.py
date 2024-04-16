class Solution(object):
    def findDisappearedNumbers(self, nums):
        #arr = []
        #minimum = min(nums)
        #for i in range(minimum, len(nums)+1):
         #   if i not in nums:
          #      arr.append(i)
            
        
        #return arr

        hashMap = defaultdict(int)
        n = len(nums)
        answerList = []
        # for all the values in nums, storing the number of its occurences
        for i in nums:
            hashMap[i] = hashMap[i] + 1
        
        #for each value in the range [1,n] , we check , if its not present in the hashmap
        # we append it to the answerList
        for i in range(1, n+1):
            if i not in hashMap:
                answerList.append(i)

        return answerList

        