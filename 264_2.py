class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly=[1]
        id=[0,0,0]
        ele=[2,3,5]
        count=1
        while count<n:
            minv=float("inf")
            sel=-1
            for i in range(3):
                if ele[i]*ugly[id[i]]<minv:
                    minv=ele[i]*ugly[id[i]]
                    sel=i
            id[sel]+=1
            if minv==ugly[-1]:
                continue
            else:
                ugly.append(minv)
                count+=1
        print(ugly)
        return ugly[-1]

a=Solution()
print(a.nthUglyNumber(10))
