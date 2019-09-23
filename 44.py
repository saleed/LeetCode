class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match(s,p)



    def match(self,s,p):
        # print(s,p,len(s),len(p))
        if len(s)==0 and len(p)==0:
            # print("11111")
            return True

        if len(s)>0 and len(p)>0:
            if p[0]==s[0]:
                return self.match(s[1:],p[1:])
            elif p[0]=='?':
                return self.match(s[1:],p[1:])
            elif p[0]=='*':
                j=0
                while j<=len(s):
                    if self.match(s[j:],p[1:]):
                        # print("2222")
                        return True
                    j+=1
            else:
                return False
        return False


# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:



# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:

# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false

a=Solution()
# print(a.isMatch("aa","*"))
print(a.isMatch("acdb","a*c?b"))
print(a.isMatch("ac","a*c"))