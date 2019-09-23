class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ele=[]
        num=[]
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
        for key,val in dict.items():
            ele.append(key)
            num.append(val)
        res=[]
        self.dfs(0,ele,num,[],res)
        return res




    def dfs(self,id,ele,num,cur,res):
        if id==len(ele):
            res.append(cur[:])
            return
        for i in range(num[id]+1):
            new=cur[:]
            new.extend([ele[id]]*i)
            self.dfs(id+1,ele,num,new,res)


print([0].extend([1]*1))

