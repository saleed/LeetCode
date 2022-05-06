class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        res=[]
        flag=1
        for i in range(0,len(mat[0])):
            x=0
            y=i
            tmp=[]
            while x<len(mat) and y>=0:
                tmp.append(mat[x][y])
                y-=1
                x+=1
            if flag==1:
                res.extend(tmp[::-1])
            else:
                res.extend(tmp[:])
            flag=flag*-1

        for i in range(1,len(mat)):
            x=i
            y=len(mat[0])-1
            tmp=[]
            while x<len(mat) and y>=0:
                tmp.append(mat[x][y])
                y-=1
                x+=1
            if flag==1:
                res.extend(tmp[::-1])
            else:
                res.extend(tmp[:])
            flag=flag*-1

        return res


