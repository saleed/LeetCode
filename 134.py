class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        i = 0
        while i < len(gas):
            curgas = 0
            flag = 0
            for j in range(len(gas)):
                if curgas + gas[(i + j) % len(gas)] < cost[(i + j) % len(gas)]:
                    i += j + 1
                    flag = 1
                    break
                else:
                    curgas+=gas[(i+j)%len(gas)]-cost[(i+j)%len(gas)]
            if not flag:
                return i
        return -1


