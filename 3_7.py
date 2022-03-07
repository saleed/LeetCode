class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        # """
        if s=="":
            return 0

        pos_set=dict()
        max_len=0
        tmp_len=0
        for i in range(len(s)):
            max_len=max(tmp_len,max_len)
            if s[i] in pos_set:
                tmp_len=i-pos_set[s[i]]
                delkey=[]
                for k in pos_set:  ####删除的很不优雅
                    if pos_set[k] <pos_set[s[i]]:
                        delkey.append(k)
                for k in delkey:
                    del pos_set[k]
                pos_set[s[i]]=i
            else:
                tmp_len+=1
                pos_set[s[i]]=i

        return max_len

        # if s=="":
        #     return 0
        # dp=[[False for _ in range(len(s))] for _ in range(len(s))]
        #
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if i>=j:
        #             dp[i][j]=True
        # maxl=1
        # for l in range(1,len(s)-1):
        #     for i in range(len(s)):
        #         if i+l>=len(s):
        #             continue
        #         if dp[i+1][i+l-1] and s[i]==s[i+l]:
        #             dp[i][i+l]=True
        #             maxl=max(maxl,l+1)
        #
        #
        # return maxl

a = Solution()
s = "abcabcbb"
print(a.lengthOfLongestSubstring(s))



