class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }


        def backTrack(i, curstr):
            if len(digits) == len(curstr):
                res.append(curstr)
                return

            for c in digitToMap[digits[i]]:
                backTrack(i + 1, curstr + c )

        backTrack(0, "")

        return res