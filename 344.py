class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """

        p=0
        q=len(s)-1
        while p<q:
            s[p],s[q]=s[q],s[p]
            p+=1
            q-=1
            