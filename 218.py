class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        buildings.sort(key=self.cmpbyleft())
        rightbuf=[]
        newbu=buildings[1:]
        rightbuf.append(0)
        while len(rightbuf)!=0 and  len(newbu)!=0:



    def cmpbyleft(self,ele,):
        return ele[0]
    def cmpbyleft(selfs,ele):
        return ele[1]


left = right = height = []
p=q=0
p=1
q=2
left.append(1)
height.append(2)
print left,height  #[1, 2] [1, 2]
print p,q  #1 2


