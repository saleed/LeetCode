class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                continue
            elif flowerbed[i]==0 and ((i-1>=0 and flowerbed[i-1]==0) or i-1<0) and (((i+1)<len(flowerbed) and flowerbed[i+1]==0) or i+1>=len(flowerbed)):
                flowerbed[i]=1
                n-=1
                if n<=0:
                    return True
        return False
            
