class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        maxR=-float("inf")
        houses.sort()
        heaters.sort()
        p=0
        q=0
        while p<len(houses):
            minv=float("inf")
            print(p, q)
            while q<len(heaters) and houses[p]>heaters[q]:
                minv=min(minv,houses[p]-heaters[q])
                q+=1
            if q!=len(heaters):
                minv=min(heaters[q]-houses[p],minv)
            if q>0:
                q-=1
            if minv!=float("inf"):
                maxR=max(minv,maxR)
            p+=1
        return maxR


ss=Solution()
house=[1,2,3]
heat=[2]
print(ss.findRadius(house,heat))
