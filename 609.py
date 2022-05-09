class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """


        cdict={}
        for v in paths:
            spv=v.split(" ")
            dir=v[0]
            for fn in spv[1:]:
                mid=fn.split("(")
                content=mid[1][:-1]
                filename=mid[0]
                if content in cdict:
                    cdict[content].append(os.path.join(dir,filename))
                else


                if cdict[]
                cdict[mid:-1]