class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sp=path.split("/")
        res=[]
        p=len(sp)-1
        flag=0
        while p>=0:
            if sp[p]=="" or sp[p]==".":
                p-=1
            elif sp[p]=="..":
                p-=1
                flag+=1
            else:
                if flag:
                    flag-=1
                else:
                    res.append(sp[p])
                p-=1
        return "/"+"/".join(list(reversed(res)))

path = "/a/./b/../../c/"
a=Solution()
print(a.simplifyPath(path))