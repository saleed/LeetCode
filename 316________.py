class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s=set(list(s))
        # # print(list(s))
        # b=list(s)
        # b.sort()
        # return "".join(b)


        #思路，一个字典，保存当前出现的字符和位置；一个字符串，保存着所有字符的一个排列：
        #遇到一个字符不在集合中，直接加到字符串尾部;如果遇到一个重复字符，判断该字符与替换后字符的大小，如果替换后更小，则替换
        #考虑这样一个问题，对于给定一个字符串，将其中某一位移动到串尾部，得到的新串是否比原串大？

        #如果制定一个判断依据：
        #加入该位比后面一位大：移动后>移动前
        #。。。。。。。。。小：移动后<移动前
        #相等考虑第一个不等于该位的字符和该位字符的大小，判断同上




a=Solution()
print(a.removeDuplicateLetters("abdcd"))



l=['a','b','c','d']
print("".join(l))
