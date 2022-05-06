class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

        maxl=0
        res=""
        for d in dictionary:
            if self.match(s,d):
                print(s,d)
                if maxl<len(d) or(maxl==len(d) and res>d):
                    maxl=len(d)
                    res=d

        return res

    def match(self,s,p):
        sptr=0
        for i in range(len(p)):
            while sptr<len(s) and s[sptr]!=p[i]:
                sptr+=1

            if sptr==len(s):
                return False
            sptr += 1
        return True
test="abpcplea"
arr=["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]

ss=Solution()
print(ss.findLongestWord(test,arr))

print(ss.match(test,arr[5]))