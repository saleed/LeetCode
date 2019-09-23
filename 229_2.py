class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i]+=1
            else:
                if len(dict)==2:
                    for j in dict.keys():
                        dict[j]-=1
                        if dict[j]==0:
                            del dict[j]
                else:
                    dict[i]=1
        if len(dict)==0:
            return []
        if len(dict)==1:
            return list(dict.keys())

        newdict={}
        res=[]
        for i in dict.keys():
            newdict[i]=0
        for j in nums:
            if j in newdict.keys():
                newdict[j]+=1
        for key in newdict.keys():
            if newdict[key]>(len(nums)/3):
                res.append(key)
        return res



