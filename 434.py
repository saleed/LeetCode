class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        cnt=0
        while i<len(s):
            if s[i].isalpha():
                cnt+=1
                while i<len(s) and s[i].isalpha():
                    i+=1
            else:
                i+=1
        return cnt
test="Hello, my name is John"
a=Solution()
print(a.countSegments(test))