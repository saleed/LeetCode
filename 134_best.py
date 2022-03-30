class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        start=0
        while start<len(gas):
            gasback=0
            flag=0
            for i in range(len(gas)):
                index=(start+i)%len(gas)
                gasback+=gas[index]
                gasback-=cost[index]
                if gasback<0:
                    flag=1
                    start=start+i+1
                    break
            if flag==0:
                return start
        return -1


gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
a=Solution()
print(a.canCompleteCircuit(gas,cost))












