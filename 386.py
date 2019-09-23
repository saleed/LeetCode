class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dict=[str(i) for i in range(1,n+1)]
        dict.sort()
        for i in range(len(dict)):
            dict[i]=int(dict[i])
        return dict

a=Solution()
print a.lexicalOrder(13)
