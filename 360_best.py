class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        p=0
        q=len(nums)-1
        if a==0:
            if b<=0:
                return list(map(lambda x:b*x+c,nums))[::-1]
            else:
                return list(map(lambda x:b*x+c,nums))
        axis=float(-b)/float(2*a)
        print(axis)
        res=[]
        while p<=q:
            if abs(nums[p]-axis)>abs(nums[q]-axis):
                res.append(a*(nums[p]*nums[p])+b*nums[p]+c)
                p+=1
            else:
                res.append(a*(nums[q]*nums[q])+b*nums[q]+c)
                q-=1
        if a>0:
            return res[::-1]
        else:
            return res


