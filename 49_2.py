class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        for i in strs:
            s= "".join(sorted(i))
            if s in dict.keys():
                dict[s].append(s)
            else:
                dict[s]=[s]
        res=[]
        for val in dict.values():
            res.append(val)

        return res



a="tea"
print(str(sorted(a)))
print("".join(sorted(a)))