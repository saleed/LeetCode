class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        for i in range(len(gas)):
            curgas = 0
            j=i
            flag=0
            while j<len(gas)+i:
                curgas+=gas[j%len(gas)]
                if curgas<cost[j%len(gas)]:
                    flag=1
                    break
                curgas-=cost[j%len(gas)]
                j+=1
            if not flag:
                return i
        return -1