class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for j in list(reversed(range(len(s)/2))):



    def isPalindromeFormId(self,s,id):
        p=id
        q=id+1
        isPal=True
        while p>=0 :
            if s[p]==s[q]:
                p-=1
                q+=1
                continue
            else:
                isPal=False
        if isPal:
            return q-1

        isPal=True
        p=id-1
        q=id+1
        while p >= 0:
            if s[p] == s[q]:
                p -= 1
                q += 1
                continue
            else:
                isPal = False
        if isPal:
            return q - 1

