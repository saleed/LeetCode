class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(candidates,0,0,target,[],res)
        return res


    ##看了之前的写法，是默认了所有candidate都大于0，这样能限定一个取每个数字的个数界限
    ##假如没有candidate为正整数的限定，那解集就不能被选择判定

    def dfs(self,candidates,i,tmp_sum,target,tmp_select,res):
        # print(i,tmp_select,tmp_sum,target)
        if tmp_sum==target:
            res.append(tmp_select[:])
            return
        if i<len(candidates):
            select_num=0
            while tmp_sum+select_num*candidates[i]<=target:
                tmp_select.extend([candidates[i]]*select_num)
                self.dfs(candidates,i+1,tmp_sum+select_num*candidates[i],target,tmp_select,res)
                tmp_select=tmp_select[:len(tmp_select)-select_num]
                select_num+=1

if __name__ == "__main__":
    a=Solution()
    test=[2,3,6,7]
    target=7
    print(a.combinationSum(test,7))
    # print(test)
    test.extend([0]*5)
    print(test[:len(test)-5])
    print(test)