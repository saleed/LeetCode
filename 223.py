class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x1,x2=self.getIntersection(A,C,E,G)
        y1,y2=self.getIntersection(B,D,F,H)
        print x1,x2,y1,y2
        if x1!=-1 and y1!=-1:
            return self.getArea(A,B,C,D)+self.getArea(E,F,G,H)-(x2-x1)*(y2-y1)
        return  self.getArea(A,B,C,D)+self.getArea(E,F,G,H)

    def getIntersection(self,A,C,E,G):
        if A>E:
            A,E=E,A
            C,G=G,C
        if C<E:
            return -1,-1
        else:
            return E,min(C,G)

    def getArea(self,a,b,c,d):
        return abs(a-c)*abs(b-d)


#very clear code
def computeArea(self, A, B, C, D, E, F, G, H):
    overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
    return (A-C)*(B-D) + (E-G)*(F-H) - overlap