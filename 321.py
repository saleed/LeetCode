class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        str1=self.list2str(nums1)
        str2=self.list2str(nums2)
        res=["0"*5]
        print res
        self.dfs("",str1,str2,k,res)
        return self.str2list(res[0])
#####

    def dfs(self,cur,num1,num2,k,res):
        # print cur
        if len(num1)+len(num2)<k:
            return
        if cur<res[0][:len(cur)]:
            return
        if k==0:
            # print cur
            res[0]=cur[:]
            return
        for i in range(len(num1)):
            newcur=cur+num1[i]
            self.dfs(newcur,num1[i+1:],num2[:],k-1,res)

        for i in range(len(num2)):
            newcur = cur + num2[i]
            self.dfs(newcur, num1[:], num2[i+1:],k-1, res)
        return

    def list2str(self,l):
        res=""
        for i in l:
            res+=str(i)
        return res
    def str2list(self,s):
        res=[]
        for i in s:
            res.append(int(i))
        return res


print "">"0"


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
a=Solution()
print a.maxNumber(nums1,nums2,k)

nums1 = [1,1,3,9,1,9,2,8,6,8,9,3,9,9,8,9,7,8,0,8,3,0,3,6,0,4,6,1,6,5,0,9]
nums2=[4,7,9,5,5,1,6,9,7,5,0,4,5]
k=45
print a.maxNumber(nums1,nums2,k)