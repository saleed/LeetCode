class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """


        cdict={}
        for v in paths:

            spv=v.split(" ")
            print(spv)
            dir=v[0]
            for fn in spv[1:]:
                mid=fn.split("(")
                content=mid[1][:-1]
                filename=mid[0]
                if content in cdict:
                    cdict[content].append(os.path.join(dir,filename))
                else:
                    cdict[content]=[os.path.join(dir, filename)]


        res=[]
        for k in cdict:
            res.append(cdict[k])
        return res

