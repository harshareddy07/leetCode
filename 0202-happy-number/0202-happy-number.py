class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = getSum(slow)
            fast = getSum(getSum(fast))

            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
        

def getSum(n):
    s = 0
    while n :
        d = n % 10
        s += d * d
        n //= 10
    return s