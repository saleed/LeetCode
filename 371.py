class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a+b

    #bit operation
    # getSum(int a, int b) {
    #     int sum = a;
    #
    #     while (b != 0)
    #         {
    #             sum = a ^ b; // calculatecarry
    #             b = (a & b) << 1; // calculate the carry
    #             a = sum; // add sum (without carry) and carry
    #         }
    #
    #     return sum;
    #     }