class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        #可以给出一个公式：长度位N的等差数列包含多少个等差数列 n-2+n-3+...1 =(n-1)*(n-2)/2 比如长度位4 共有3个等差数列
        #所以本题只要求总共由多少个不相邻的等差数列即可


        if len(A)<2:
            return 0
        start=0
        end=0
        d=A[1]-A[0]
        res=0
        A.append(float("inf"))
        for i in range(2,len(A)):
            if A[i]-A[i-1]==d:
                end=i
            else:
                d=A[i]-A[i-1]
                res+=(end-start)*(end-start-1)/2
                start=i-1
                end=start

        return int(res)



a=Solution()
A=[1, 3, 5, 7, 9]
print(a.numberOfArithmeticSlices(A))
A=[1,2,3,4]
print(a.numberOfArithmeticSlices(A))




