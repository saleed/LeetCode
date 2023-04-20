class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """


        presum=[[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                if i==0 and j==0:
                    presum[i][j]=img[i][j]
                elif i==0:
                    presum[i][j]=img[i][j]+presum[i][j-1]
                elif j==0:
                    presum[i][j]=img[i][j]+presum[i-1][j]
                else:
                    presum[i][j]=img[i][j]+presum[i-1][j]+presum[i][j-1]-presum[i-1][j-1]



        res=[[0 for _ in range(len(img[0]))] for _ in range(len(img))]


        for i in range(len(img)):
            for j in range(len(img[0])):
                y1=min(len(img[0])-1,j+1)
                x1=min(len(img)-1,i+1)
                y2=max(0,j-1)
                x2=max(0,i-1)

                res[i][j]=presum[x1][y1]-img[i][j]
                if x2>=0:
                    res[i][j]-=presum[x2][y1]
                if y2>=0:
                    res[i][j]-=presum[x1][y2]
                if x2>=0 and y2>=0:
                    res[i][j]+=presum[x1][y1]
                res[i][j]=int(res[i][j]/8)
        return res

[[100,200,100],
 [200,50,200],
 [100,200,100]]

[[61,94,61],[94,138,94],[61,94,61]]


[[137,141,137],[141,138,141],[137,141,137]]

