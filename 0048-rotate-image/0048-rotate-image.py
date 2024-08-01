class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        left = 0
        right = len(matrix) -1 

        while left < right:
            for i in range(right-left):
                top = left 
                bottom = right
                # save the topleft in temp
                temp = matrix[top][left+i]

                # move  bottomleft to topleft
                matrix[top][left+i] = matrix[bottom-i][left]

                # move bottomright to bottomleft
                matrix[bottom-i][left] = matrix[bottom][right-i]

                # move topright to bottomright
                matrix[bottom][right-i] = matrix[top+i][right]

                # move temp to topright
                matrix[top+i][right] = temp

            left += 1
            right -= 1

 
            
            


        