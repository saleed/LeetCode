class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num)<3:
            return False

        for i in range(len(num)-2):
            for j in range(i+1,len(num)-1):
                if self.dfs(num[:i+1],num[i+1:j+1],num[j+1:]):
                    return True
        return False




    def dfs(self,pre1,pre2,left):
        print(pre1,pre2,left)
        if pre1[0]=='0' and len(pre1)!=1:
            return False
        if pre2[0]=='0' and len(pre2)!=1:
            return False
        if len(left)==0:
            return True
        if left[0]=='0':
            if int(pre1) + int(pre2) == 0 and self.dfs(pre2,'0',left[1:]):
                return True
            else:
                return False
        for i in range(len(left)):
            if int(pre1)+int(pre2)==int(left[:i+1]) and self.dfs(pre2,left[:i+1],left[i+1:]):
                return True
        return False


a=Solution()
t="1023"
print(a.isAdditiveNumber(t))


