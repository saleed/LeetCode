class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        count=0
        while pow(10,i-1)<=n:
            # print n/10,min(max((n)%pow(10,i)-pow(10,i-1)+1,0),pow(10,i-1))
            count+=(n)/pow(10,i)*pow(10,i-1)+min(max((n)%pow(10,i)-pow(10,i-1)+1,0),pow(10,i-1))
            i+=1
        return count


n=13
a=Solution()
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
print a.countDigitOne(n)

