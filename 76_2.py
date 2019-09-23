class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l=0
        r=0
        minlen=len(s)
        req=set()
        search={}
        for i in t:
            req.add(i)
            search[i]=0
        print(req)
        while r<len(s)-1:####这里的循环条件有问题
            print(r,l,req,search)
            if len(req)>0:
                if s[r] in search.keys():
                    search[s[r]]+=1
                    if s[r] in req:
                        req.remove(s[r])
                r+=1   ####问题在于
            else:
                # if minlen>r-l:
                # print(r,l)
                minlen=min(r-l+1,minlen)
                if s[l] in search.keys():
                    search[s[l]]-=1
                    if search[s[l]]==0:
                        req.add(s[l])
                l += 1
        return minlen


a=Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(S[12])
print(a.minWindow(S,T))

a=set()
a.add(1)
b=set()
b.add(1)
print(a==b)
dict={}
dict[1]=1
dict[2]=2
print(set(dict.keys()))











a=set()
a.add(1)
a.add(1)
a.remove(1)
# a.remove(2)


