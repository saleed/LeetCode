class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        hashdict={}
        for v in s:
            if v in hashdict:
                hashdict[v]+=1
            else:
                hashdict[v]=1
        flag=0
        tmp=""
        for v in hashdict:
            if len(s)%2==0 and hashdict[v]%2!=0:
                return []
            elif len(s)%2==1 and hashdict[v]%2==1:
                if flag==0:
                    flag=1
                    tmp=v
                else:
                    return []

        res=[]
        self.dfs(hashdict,tmp,res)
        return res

    def dfs(self,hashdict,tmp,res):
        find=0
        for v in hashdict:
            if hashdict[v]==1:
                continue
            elif hashdict[v]>0:
                find=1
                hashdict[v]-=2
                tmp=v+tmp+v
                self.dfs(hashdict,tmp,res)
                hashdict[v]+=2
                tmp=tmp[1:-1]
        if find==0:
            res.append(tmp[:])




