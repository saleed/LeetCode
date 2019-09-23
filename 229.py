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
                if len(dict.keys())==3:
                    dict=self.updateDic(dict)
                dict[i]=1
        res=[]
        print dict
        for key in dict.keys():
            dict[key]=0
        for i in nums:
            if i in dict.keys():
                dict[key]+=1
        for key in dict.keys():
            if dict[key]>len(nums)/3:
                res.append(key)
        return res

    def updateDic(self,dict):
        flag=1
        while flag:
            for i in dict.keys():
                if dict[i]>0:
                    dict[i]-=1
                if dict[i]==0:
                    del dict[i]
                    flag=0
        return dict



dict={}
print len(dict.keys())

test=[3,2,3]
a=Solution()
print a.majorityElement(test)


