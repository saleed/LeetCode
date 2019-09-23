class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict={2:0,3:0,5:0}
        minv=0
        res=[]
        pre=-1
        for i in range(0,n):
            while True:
                minv = float("inf")
                for key in dict.keys():
                    if pow(key,dict[key]+1)<minv:
                        minv=pow(key,dict[key])
                        k=key
                dict[k]+=1
                if minv>pre:
                    break
            pre=minv
            res.append(minv)
        return minv,res
        # return minv

a=Solution()
print a.nthUglyNumber(11)\



def nthUglyNumber1111(self, n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]



