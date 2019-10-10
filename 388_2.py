#解法1：构造一棵树，多叉树，然后对数使用递归深度遍历，求最大深度，比较麻烦，容易理解
#解法2：DFS思想，使用栈保存当前父目录的深度和路径长度
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        st=[]
        id=0
        maxlen=0
        maxstr=""
        offset=0
        while id<len(input):
            # print(offset)
            #记录头端id
            ptr=id
            #使用ptr往后查找单词
            while  ptr<len(input) and  input[ptr]!='\n' and  input[ptr]!='\t':
                ptr+=1
            tmpstr=input[id:ptr]
            #查找到单词后，根据当前单词的偏移和长度，更新堆栈
            if len(st)==0:
                st.append((tmpstr,len(tmpstr),offset))
            else:
                while len(st)>0:
                    top=st[-1]
                    if top[2]>=offset:
                        st.pop()
                    else:
                        break
                if len(st)==0:
                    st.append((tmpstr,len(tmpstr),offset))
                else:
                    st.append((tmpstr,st[-1][1]+len(tmpstr),offset))

                if maxlen < st[-1][1]:
                    maxlen = st[-1][1]
                    maxstr = self.constructSt(st)
            #查找下个单词的偏移
            while  ptr<len(input) and ( input[ptr]=='\n' or input[ptr]=='\t'):
                if input[ptr]=='\n':
                    offset=0
                else:
                    offset+=1
                ptr+=1
            id=ptr
        return maxstr


    def constructSt(self,st):
        ret=""
        for i in range(len(st)):
            ret+="\\n"+i*"\\t"+str(st[i][0])
        return ret[2:]




a=Solution()
input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(a.lengthLongestPath(input))















