import  math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        l=int(math.sqrt(area))
        w=l
        while l*w!=area and l<=area:
            if l*w<area:
                l=(area+l+1)/2
            else:   
                w=w/2
        return [int(l),int(w)]


ss=Solution()
area=37
print(ss.constructRectangle(area))