class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        minid=[0]*len(primes)
        ugly=[1]
        i=1
        while i<n:
            selid=-1
            minval=float("inf")
            for j in range(len(primes)):
                if ugly[minid[j]]*primes[j]<minval:
                    minval=ugly[minid[j]]*primes[j]
                    selid=j
            minid[selid] += 1
            if minval==ugly[-1]:
                continue
            ugly.append(minval)
            i+=1
        print(ugly)
        return ugly[-1]

a=Solution()
n=12
t=[2,7,13,19]
print(a.nthSuperUglyNumber(n,t))