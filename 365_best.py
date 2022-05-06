class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        vis=set()
        return self.dfs(jug1Capacity,jug2Capacity,0,0,targetCapacity,vis)

    def dfs(self,x,y,xremain,yremain,target,vis):
        if xremain>x or yremain>y or xremain<0 or yremain<0:
            return False
        if xremain==target or yremain==target or yremain+xremain==target:
            return True
        if (xremain,yremain) in vis:
            return False
        vis.add((xremain,yremain))
        return self.dfs(x,y,x,yremain,target,vis) or self.dfs(x,y,xremain,y,target,vis) or self.dfs(x,y,0,yremain,target,vis) \
               or self.dfs(x,y,xremain,0,target,vis) or self.dfs(x,y,xremain-yremain,0,target,vis) or self.dfs(x,y,0,yremain-xremain,target,vis)








