class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        pairdict={"0":"0","1":"1","8":"8","6":"9","9":"6"}
        if n==1:
            return ["1","0","8"]
        res=[]
        self.dfs2(n,"",res,pairdict)
        return res








    def dfs2(self,n,tmp,res,pairdict):
        if len(tmp)==n:
            if tmp[0]=='0':
                return
            if n%2==1 and tmp[n/2] in ("6","9"):
                return
            res.append(tmp[:])
        else:
            for v in pairdict:
                if n%2==1 and len(tmp)==0:
                    tmp=v
                    self.dfs2(n,tmp,res,pairdict)
                    tmp=""
                else:
                    tmp=v+tmp+pairdict[v]
                    self.dfs2(n,tmp,res,pairdict)
                    tmp=tmp[1:-1]














####

    def dfs1(self,n,pairlist,res,tmp):
        if(n%2==0 and len(tmp)<n/2)  or (n%2==1 and len(tmp)<=n/2):
            for v in pairlist:
                tmp+=str(v)
                self.dfs(n,pairlist,res,tmp)
                tmp=tmp[:-1]
        else:
            # print tmp
            newtmp=tmp[:]
            for i in range(len(tmp))[::-1]:
                if n%2==0:
                    newtmp+=str(pairlist[int(tmp[i])])
                else:
                    if i-1>=0:
                        newtmp+=str(pairlist[int(tmp[i-1])])
            res.append(newtmp)


a=Solution()
print(a.findStrobogrammatic(2))






