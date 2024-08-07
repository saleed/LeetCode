class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=str(n)
        if len(l)==1:
            return n-1
        id=-1
        for i in range(1,len(l)):
            if l[i]<=l[i-1]:
                id=i-1
                break
        if id==-1:
            return n
        res=l[:id]+str(int(l[id])-1)+'9'*(len(l)-(id+1))
        return int(res)
