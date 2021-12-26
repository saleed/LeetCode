class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        map_dict={}

        target_set=set()
        for i in range(len(s)):
            if s[i] in map_dict and map_dict[s[i]]==t[i]:
                continue
            elif s[i] not in map_dict and t[i] not in target_set:
                map_dict[s[i]]=t[i]
                target_set.add(t[i])
            else:
                return False
        return True


    def errSolution1(self,s,t):
        map_dict={}
        for i in range(len(s)):
            if s[i] in map_dict and map_dict[s[i]]==t[i] and t[i] in map_dict and map_dict[t[i]]==s[i]:
                continue
            elif s[i] not in map_dict and t[i] not in map_dict:
                map_dict[s[i]]=t[i]
                map_dict[t[i]]=s[i]
            else:
                return False
        return True
