class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """

        list1="12"
        list2="122"

        while len(list2)<n:
            nextch="1"
            if list2[-1]=="1":
                nextch="2"
            chnum=int(list2[len(list1)])
            list2+=nextch*chnum
            list1+=list2[len(list1)]
            # print(list1,list2)
        cnt=0
        print(list1,list2)
        for v in list2[:n]:
            if v=="1":
                cnt+=1
        return cnt



ss=Solution()
print(ss.magicalString(6))















