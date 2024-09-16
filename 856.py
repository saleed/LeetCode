class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if s=="()":
            return 1
        st=1
        id=-1
        for i in range(1,len(s)):
            if s[i]=="(":
                st+=1
            else:
                st-=1
            if st==0:
                id=i
                break
        left=self.scoreOfParentheses(s[1:id])
        right=self.scoreOfParentheses(s[id+1:])
        if left==0:
            return 1+right
        else:
            return 2*left+right


