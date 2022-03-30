class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num)==0:
            return None
        res=[]
        cnt=0
        i=0
        while i<len(num):
            if cnt==k:
                res.append(num[i])
                i+=1

                continue
            else:
                if len(res)>0 and num[i]<=res[-1]:
                    res.pop()
                    cnt+=1
                else:
                    res.append(num[i])
                    i+=1
        return "".join(res[:len(num)-k+1])






