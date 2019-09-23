class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res=[1]
        pos=[0]*len(primes)
        while len(res)<n:
            minv=float("inf")
            sel=0
            for j in range(len(primes)):
                if minv>res[pos[j]]*primes[j]:
                    minv=res[pos[j]]*primes[j]
                    sel=j
            if minv>res[-1]:
                res.append(minv)
            print pos,res
            pos[sel]+=1
        print res

        return res[-1]


n = 12
primes = [2,7,13,19]

a=Solution()
a.nthSuperUglyNumber(n,primes)

