class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)<=0:
            return
        valarr,numarr=self.process(candidates)
        print(valarr,numarr)
        res=[]
        self.dfs(valarr,numarr,0,target,[],res)
        return res



    def process(self,candidates):
        dict={}
        for i in candidates:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
        valarr=[]
        numarr=[]
        for key,val in dict.items():
            valarr.append(key)
            numarr.append(val)
        return valarr,numarr





    #编程参数方法论：
        # 源头资源: valarr,numarr
        # 操作中间值:id,cursel,left
        # 目标值:res

    def dfs(self,valarr,numarr,id,left,cursel,res):
        if left==0:
            res.append(cursel[:])
        else:
            if id<len(valarr):
                for k in range(numarr[id]+1):
                    if left-valarr[id]*k>=0:
                        # print(cursel)
                        newsel=cursel[:]
                        newsel.extend(k*[valarr[id]])
                        self.dfs(valarr,numarr,id+1,left-valarr[id]*k,newsel,res)

candidates = [10,1,2,7,6,1,5]
target = 8
a=Solution()
print(a.combinationSum2(candidates,target))