class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        id=len(arr)
        for i in range(len(arr)):
            if arr[i]>=x:
                id=i
                break
        p=id-1
        q=id
        res=[]
        while (p>=0 or q<len(arr)) and len(res)<k:
            pval=abs(x-arr[p]) if p>=0 else float("inf")
            qval=abs(x-arr[q]) if q<len(arr) else float("inf")
            if pval<=qval:
                res=[arr[p]]+res
                p-=1
            else:
                res.append(arr[q])
                q+=1
        return res




