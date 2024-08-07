class Solution(object):
    def removeDuplicateLetters(self, num):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        ldict={}
        for v in num:
            if v in ldict:
                ldict[v]+=1
            else:
                ldict[v]=1

        i=0
        st=[]
        while i<len(num):
            print(ldict,st)
            ##如果是重复的字符，加在后面？为什么直接跳出这个
            if num[i] not in st:
            ###
                while len(st)>0 and st[-1]>num[i] and ldict[st[-1]]>0:
                    st.pop()
                st.append(num[i])
            ###记录数剩余的字符个数
            ldict[num[i]] -= 1
            i+=1
        return "".join(st)

test="bcabc"
s=Solution()
print(s.removeDuplicateLetters(test))