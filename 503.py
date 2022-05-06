class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortlist=[]
        i=0
        res=[]
        while i<len(nums):
            start=(i+1)%len(nums)
            q=len(sortlist)-1
            while q>=0 and nums[sortlist[q][0]]>=nums[i]: ########>=
                q-=1
            if q>=0:
                start=max(i+1,sortlist[q][1])%len(nums)
            print(start,sortlist)
            p=start
            while p != i and nums[p] <= nums[i]:#####<=
                p=(p+1)%len(nums)
            if p == i:
                res.append(-1)
            else:
                l1=sortlist[:start+1]
                l1.append([i,p])
                l1.extend(sortlist[start+1:])
                sortlist=l1
                res.append(nums[p])
            i+=1
        return res


ss=Solution()
test=[1,2,3,4,5,6,5,4,5,1,2,3]
print(ss.nextGreaterElements(test))