class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sp=path.split("/")
        res=[]
        for v in sp:
            if v=="" or v==".":
                continue
            elif v==".." and len(res)>0:
                res.pop() 
            else:
                res.append(v)
        return "/"+"/".join(res)



path = "/a/./b/../../c/"
a=Solution()
print(a.simplifyPath(path))