from functools import cmp_to_key
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points=[p1,p2,p3,p4]
        points=sorted(points)
        a=self.toVec(points[0],points[1])
        b=self.toVec(points[0],points[2])
        c=self.toVec(points[1],points[3])
        d=self.toVec(points[2],points[3])
        print(self.innerProduct(a, b) == 0)
        print(self.innerProduct(a, c) == 0)
        print(self.innerProduct(b, d) == 0)
        return self.innerProduct(a,b) ==0 and self.innerProduct(a,c)==0 \
               and self.innerProduct(b,d)==0 and self.dist(points[0],points[1])==self.dist(points[0],points[2])==self.dist(points[2],points[3])!=0


    def toVec(self,p1,p2):
        return [p2[0]-p1[0],p2[1]-p1[1]]

    def innerProduct(self,a,b):
        return a[0]*b[0]+a[1]*b[1]

    def dist(self,x0,x1):
        return math.pow(x0[0]-x1[0],2)+math.pow(x0[1]-x1[1],2)

    def cmp(self,a,b):
        if a[0]==b[0]:
            return a[1]<b[1]
        else:
            return a[0]<b[0]
