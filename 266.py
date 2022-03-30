class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashdict={}
        for v in s:
            if v in hashdict:
                hashdict[v]+=1
            else:
                hashdict[v]=1
        flag=0
        for v in hashdict:
            if len(s)%2==0 and hashdict[v]%2!=0:
                return False
            elif len(s)%2==1 and hashdict[v]%2==1:
                if flag==0:
                    flag=1
                else:
                    return False

