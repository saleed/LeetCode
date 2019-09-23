#low level comprehesion

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        dict={}
        for i in s:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
        pos=0
        for i in range(len(s)):
            if s[i]<s[pos]:
                pos=i
            dict[s[i]]-=1
            if dict[s[i]]==0:
                break
        news=s[pos+1:].replace(s[pos],"")
        return s[pos]+self.removeDuplicateLetters(news)
input="bcabc"
a=Solution()
print a.removeDuplicateLetters(input)

# print input.replace('b',"")
# print input