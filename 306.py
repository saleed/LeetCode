class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pre1=0


    def dfs(self,left,pre1,pre2):
        if len(left)==0:
            return True
        for i in range(len(left)):
            if left[0]=='0' and pre1+pre2!=0:
                break
            sel=int(left[:i+1])
            if pre1+pre2==sel:
                self.dfs(left[i+1:],pre2,sel)
        return False

