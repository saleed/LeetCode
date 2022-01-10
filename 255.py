####err solution

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        return self.dfs(preorder)



    def dfs(self,preorder):
        if len(preorder)==0:
            return True
        else:
            root=preorder[0]
            i=0
            while i<len(preorder):
                if preorder[i]<root:
                    i+=1
                else:
                    break

            j=i
            while j<len(preorder):
                if preorder[j]<root:
                    return False
                j+=1
            return self.dfs(preorder[1:i]) and self.dfs(preorder[i:])
