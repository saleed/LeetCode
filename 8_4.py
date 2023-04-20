class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = ""
        stat = 0
        flag = 1
        i = 0
        while True:
            while i < len(s) and s[i] == " ":
                i += 1
            stat = 1
            if i < len(s):
                if s[i] == "-":
                    flag = -1
                    i += 1
                elif s[i] == "+":
                    i += 1

            while i < len(s) and s[i].isdigit():
                res += s[i]
                i += 1
            break

        if res.isdigit():
            if flag * int(res) <= -pow(2, 31):
                return -pow(2, 31)
            if flag * int(res) >= pow(2, 31) - 1:
                return pow(2, 31) - 1
            return flag * int(res)
        else:
            return 0




