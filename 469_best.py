class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        pre=0
        l=len(points)
        for i in range(len(points)):
            x1=points[(i+1)%l][0]-points[i%l][0]
            y1=points[(i+1)%l][1]-points[i%l][1]

            x2=points[(i+2)%l][0]-points[(i+1)%l][0]
            y2=points[(i+2)%l][1]-points[(i+1)%l][1]

            product=x1*y2-x2*y1
            if product!=0:  ##??????
                if pre*product<0:
                    return False
                pre=product
        return True


