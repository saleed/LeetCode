class Solution(object):
    def multiply(self, mat1, mat2):
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """

        mat1dict={}
        mat2dict={}

        for i in range(len(mat1)):
            mat1dict[i]={}
            for j in range(len(mat1[0])):
                mat1dict[i][j]=mat1[i][j]

        for i in range(len(mat2[0])):
            mat2dict[i] = {}
            for j in range(len(mat2)):
                mat2dict[i][j] = mat2[i][j]

        res=[[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                sum=0
                for k in mat1dict[i]:
                    if k in mat2dict[j]:
                        sum+=mat1dict[i][k]*mat2dict[j][k]
                res[i][j]=sum
        return res



