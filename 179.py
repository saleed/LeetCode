class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res=[]
        for i in nums:
            res.append(str(i))
        # print res
        res.sort(key=lambda x,y: cmp_to_key(y+x, x+y))  #the key sentence
        print res
        rlt=""
        for i in res:
            if rlt=='0' and i=='0':
                continue
            rlt+=i
        return rlt


a=Solution()
Input= [3,30,34,5,9]
# Output: "9534330"
print a.largestNumber(Input)
print "91">"91111"

