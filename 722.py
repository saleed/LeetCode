class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        sstr = "\n".join(source)
        # print(sstr)
        ret = self.trimStr(sstr)
        res=ret.split("\n")
        # print(res)
        newres=[]
        for v in res:
            if v!="":
                newres.append(v)
        return newres

    def trimStr(self, source):
        i = 0
        res = ""
        while True:
            if i + 1 < len(source) and source[i:i + 2] == "//":
                j = i+2  ##这里写成了
                while j < len(source) and not source[j:j + 1] == '\n':
                    j += 1  ###这里写成了j+2
                i = j ##这里赋值写成了i=j+1 遇到回车不删除
            elif i + 1 < len(source) and source[i:i + 2] == "/*":
                j = i+2
                while j + 1 < len(source) and not source[j:j + 2] == "*/":
                    j += 1
                i = j + 2
            else:
                if i < len(source):
                    res += source[i]
                    i += 1
                else:
                    break
        # print(res)
        return res


