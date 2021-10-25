class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        i=0
        while i<len(gas):
            j=0
            tmpgas=0
            tmpcost=0
            flag=1
            while j<len(gas):
                tmpcost+=cost[(i+j)%len(gas)]
                tmpgas+=gas[(i+j)%len(gas)]
                if tmpcost>tmpgas:
                    flag=0
                j+=1
            if flag:
                return i
            else:
                i=i+j
        return -1


