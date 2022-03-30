class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i=0
        while i <len(matrix)/2:
            j=0
            while j <len(matrix)-i*2-1:
                print([i,i+j],[len(matrix) - 1 - i - j,i],[len(matrix) - 1 - i,len(matrix) - 1 - i - j], [i + j,len(matrix)-1 - i])
                tmp=matrix[i][i+j]
                matrix[i][i+j]=matrix[len(matrix)-1-i-j][i]
                matrix[len(matrix) - 1 - i - j][i]=matrix[len(matrix)-1-i][len(matrix)-1-i-j]
                matrix[len(matrix) - 1 - i][len(matrix) - 1 - i - j]=matrix[i+j][len(matrix)-1-i]
                matrix[i + j][len(matrix)-1 - i]=tmp

                j+=1
            i+=1
        print(matrix)

a=Solution()
mt = [[1,2,3],[4,5,6],[7,8,9]]
print(a.rotate(mt))