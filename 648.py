class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        wt=wordTree()
        for d in dictionary:
            wt.add(d)
        res=[]
        print(wt.worddict)
        for s in sentence.split(" "):
            suffix=wt.startwith(s)
            if suffix!="":
                res.append(suffix)
            else:
                res.append(s)
        return " ".join(res)

class wordTree:
    def __init__(self):
        self.worddict={}



    def add(self,word):
        tmpnode=self
        for v in word:
            if v in tmpnode.worddict:
                tmpnode=tmpnode.worddict[v]
            else:
                tmpnode.worddict[v]=wordTree()
                tmpnode=tmpnode.worddict[v]
        tmpnode.worddict["end"]=1

    def startwith(self,word):
        tmpnode=self
        tmpstr=""
        for v in word:
            if "end" in tmpnode.worddict:
                return tmpstr
            else:
                if v in tmpnode.worddict:
                    tmpnode=tmpnode.worddict[v]
                    tmpstr+=v
                else:
                    return ""
        return word



ss=Solution()
dict=["cat","bat","rat"]
st="the cattle was rattled by the battery"
print(ss.replaceWords(dict,st))






