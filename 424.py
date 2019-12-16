class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict=[0]*26
        tail=0
        res=0
        for i in range(len(s)):
            # print(i,tail,dict)
            dict[ord(s[i])-ord('A')]+=1
            maxv=max(dict)
            while i-tail+1-maxv>k:
                dict[ord(s[tail])-ord('A')]-=1
                tail+=1
                maxv=max(dict)
                # print(maxv)
            if i-tail+1>res:
                res=i-tail+1

        return res


s = "AABABBA"
k = 1



print(ord('A'))
a=Solution()
print(a.characterReplacement(s,k))


