class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """







    def input2List(self,input):
        i=0
        s=0
        res=[]
        while i<len(input):
            while input[i]<='9' and input[i]>='0':
                i+=1
            res.append(input[s:i])
            if i<len(input):
                res.append(s[i])
                i+=1
        ret=[]
        for i in res:
            if res!='*' and res!='+':
                ret.append(str(i))
            else:
                ret.append(i)
        return ret
    def interator(self,left,res,cur):
        # if len(left)==0:
        #     return 0
        if left<=0:
            new=copy.deepcopy(cur)
            res.append(new)
        elif len(left)>0:
            new=0
            if left[0]=='+':
                new=cur+int(left[0])
            if left[0] == '-':
                new=cur-int(left[0])
            if left[0]=='*':
                new=cur*int(left[0])
            self.interator(
