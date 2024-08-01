class Solution(object):
            
 
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row = [False] * len(matrix)
        column = [False] * len(matrix[0])


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    column[j] = True

        
        for i in range(len(matrix)):
            if row[i]:
                nullifyRows(matrix, i)

        for j in range(len(matrix[0])):
            if column[j]:
                nullifyColumns(matrix, j)



def nullifyRows(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0

def nullifyColumns(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0