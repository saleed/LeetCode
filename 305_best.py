class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        island=[]
        res=0
        for i in positions:
            num=0
            for i in range(len(island)):
                flag=0
                for v in island[i]:
                    if self.adjacent(positions[i][0],positions[i][1],v[0],v[1]):
                        num+=1
                        flag=1
                        break

            if num==0:
                island.append(positions[i])
                res+=1
            elif num>1:
                res=res-num+1
            else:
                continue
        return res


    def adjacent(self,r1,c1,r2,c2):
        if (r1==r2 and abs(c1-c2)==1) or (c1==c2 and abs(r1-r2)==1):
            return True
        return False
