class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs)==0:
            return 0
        pairs.sort(key=lambda x:x[0])
        print(pairs)
        top=pairs[0]
        cnt=1
        for i in range(1,len(pairs)):
            if pairs[i][0]>top[1]:
                cnt+=1
                top=pairs[i]
            else:
                if pairs[i][1]<top[1]:
                    top=pairs[i]
        return cnt





ss=Solution()
test=[[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]

print(ss.findLongestChain(test))