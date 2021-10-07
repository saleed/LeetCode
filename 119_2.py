class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]

        tmp_list=[1,1]
        for i in range(2,rowIndex+1):
            pre_list=tmp_list
            tmp_list=[1]
            for i in range(1,len(pre_list)):
                tmp_list.append(pre_list[i]+pre_list[i-1])
            tmp_list.append(1)

        return tmp_list

if __name__ == "__main__":
    a = Solution()
    print(a.getRow(3))

