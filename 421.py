class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ss=set()
        mask=0
        res=0
        for i in range(32)[::-1]:
            mask=mask|(1<<i)
            for val in nums:
                ss.add(val&mask)
                # print("insert:",format(val&mask,'b'))

            t=res|(1<<i)
            for val in nums:
                if (mask&val)^t in ss:
                    print(val,(mask&val)^t,t)
                    res = res|(1<<i)
                    break

            # print("res:", format(res, 'b'), "flag:", flag)
        return res




a=Solution()
test= [3, 10, 5, 25, 2, 8]
print(a.findMaximumXOR(test))



# 异或运算类的题目，技巧性很强。难以捉摸具体的套路。
#
# 一般都是一题一种解法。
#
# 本题中，求最大值。直观上，高位的1越多数值越大。
#
# 从高位向低位依次猜测每个位的值是1还是0.
#
# 对一个数字a，设a[i:31]表示第i位到第31位的bit值。设a[i]表示第i位的bit值。
#
# 设最大异或值为X。
#
# 先假设X在位置i上的bit为1，即X[i]=1。
#
# 接下来要确认X[i]=1是否真的可行。
#
# 考虑数字序列A，将A中每个元素A[j]的第i位到第31位都取出，存入集合S；
#
# for(j < A.length){
#     取A[j][i:31]入S；
# }
# 然后将X[i:31]与每个元素A[j][i:31]异或，如果异或值在S中，说明X[i]为1是可行的。







