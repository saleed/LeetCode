class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ch_dict=set(s1)
        window_set=set(s2[:len(s1)])
        if ch_dict==window_set:
            return True
        for i in range(len(s1),len(s2)):
            window_set.remove(s2[i-len(s1)])
            window_set.add(s2[i])
            if  ch_dict==window_set:
                return True
        return False



if __name__=="__main__":
    s1 = "adc"
    s2 = "dcda"
    a=Solution()
    print(a.checkInclusion(s1,s2))













test="1245241"
print(set(test))
