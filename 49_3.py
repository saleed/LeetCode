class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        set_dict={}
        for val in strs:
            # print(list(val))
            sort_val=list(val[:])
            sort_val.sort()
            sort_val="".join(sort_val)
            if sort_val in set_dict.keys():
                set_dict[sort_val].append(val)
            else:
                set_dict[sort_val]=[val]
        res=[]
        for val in set_dict.keys():
            res.append(set_dict[val])
        return res






if __name__=="__main__":
    a="eat"
    b="ate"
    print(set(a)==set(b))
    test= ["eat", "tea", "tan", "ate", "nat", "bat"]
    a=Solution()
    print(a.groupAnagrams(test))
