class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # dp=[[] for _ in range(len(num))]:
        #
        for i in range(len(num)-1):
            for j in range(i):
                if num[j+1]=='0' and (j+1!=i):
                    continue
                pre=[int(num[:j+1]),int(num[j+1:i+1])]
                if self.dfs(num,i+1,pre):
                    return True
        return False

    def dfs(self,nums,i,pre):
        if i==len(nums):
            return True
        tmp=str(sum(pre))
        if nums[i:i+len(tmp)]==tmp:
            pre.append(sum(pre))
            pre=pre[1:]
            return self.dfs(nums,i+len(tmp),pre)
        return False

s=Solution()
print(s.isAdditiveNumber("000"))