class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window_set={}
        max_len=0
        i=0
        while i< len(s):
            if s[i] not in window_set.keys():
                window_set[s[i]]=i
                max_len=max(max_len,len(window_set))
                i+=1
            else:
                for key in window_set.keys():
                    if window_set[key]<window_set[s[i]]:
                        del window_set[key]

                window_set[s[i]]=i
                i = window_set[s[i]] + 1

        return max_len


