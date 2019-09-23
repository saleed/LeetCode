class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.reverse(s,0,len(s)-1)
        p=q=0
        while p<len(s) and q<len(s):
            while q!=' ' and q<len(s):
                q+=1
            if q<len(s):
                self.reverse(s,p,q)
            else:
                self.reverse(s,p,q-1)
            p=q


    def reverse(self,s,i,j):
        while i<j:
            tmp=s[i]
            s[i]=s[j]
            s[j]=tmp
        return

test="the sky is blue"
a=Solution()
a.reverseWords(test)


print(int("-23"))