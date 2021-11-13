class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == right:
            return left

        res = 0
        i = 0

        while pow(2, i) < max(left, right):
            T = pow(2, i + 1)
            l1 = left % T
            r1 = right % T
            div1 = left / T
            div2 = right / T

            if div1 == div2 and l1 >= pow(2, i) and r1 >= pow(2, i):
                res += pow(2, i)
            i += 1

        return res

