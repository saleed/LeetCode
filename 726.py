class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        d=self.dfs(formula)
        keys=d.keys()
        keys.sort()
        res=""
        for k in keys:
            res+=k+str(d[k])
        return res



    def dfs(self,formula):
        print(formula)
        if formula=="":
            return {}
        if formula[0]=="(":
            lb=1
            i=1
            while i<len(formula) and lb>0:
                if formula[i]==")":
                    lb-=1
                elif formula[i]=="(":
                    lb+=1
                i+=1
            d1=self.dfs(formula[1:i])
            mul=1
            j=i
            for j in range(len(formula)):
                if not formula[j].isdigit():
                    break
            if i!=j:
                mul=int(formula[i:j+1])
            d2=self.dfs(formula[j+1:])
            for k in d1:
                d1[k]=mul*d1[k]
            for k in d2:
                if k not in d1:
                    d1[k]=d2[k]
                else:
                    d1[k]+=d2[k]
            return d1[k]
        else:
            i=0
            while i<len(formula) and formula[i].isalpha():
                i+=1
            ch=formula[:i]
            j=i
            while j<len(formula) and formula[j].isdigit():
                j+=1
            mul=1
            if i!=j:
                mul=int(formula[i:j])
            d1={ch:mul}
            d2=self.dfs(formula[j:])
            for k in d2:
                if k in d1:
                    d1[k]+=d2[k]
                else:
                    d1[k]=d2[k]
            return d1







