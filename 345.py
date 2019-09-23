class Solution(object):
    def reverseVowels(self, In):
        """
        :type s: str
        :rtype: str
        """

        p=0
        q=len(In)-1
        s=list(In)
        print s
        while p<q:
            while not self.isVowel(s[p]) and p<q:
                p+=1
            while not self.isVowel(s[q]) and p<q:
                q-=1
            if p>=q:
                break
            s[p],s[q]=s[q],s[p]
            p+=1
            q-=1
        return "".join(s)

    def isVowel(self,c):
        return c.lower()=='a' or c.lower()=='o' or c.lower()=='e' or c.lower()=='i' or c.lower()=='u'

Input="hello"
a=Solution()
print a.reverseVowels(Input)
