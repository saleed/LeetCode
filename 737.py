class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1)!=len(sentence2):
            return False

        uf=UnionFind()

        for v in similarPairs:
            uf.merge(v[0],v[1])
        print(uf.dict)

        for i in range(len(sentence2)):
            if uf.find(sentence2[i])!=uf.find((sentence1[i])):
                return False
        return True

class UnionFind:
    def __init__(self):
        self.dict={}

    def add(self,str):
        if str in self.dict:
            return
        self.dict[str]=str

    def merge(self,str1,str2):
        if str1 not in self.dict:
            self.dict[str1] = str1
        if str2 not in self.dict:
            self.dict[str2] = str2

        self.dict[self.find(str1)]=self.find(str2)
        return True

    def find(self,str1):
        if str1 not in self.dict:
            return str1
        if self.dict[str1]==str1:
            return str1
        return self.find(self.dict[str1])

    def compare(self,str1,str2):
        return self.find(str1)==self.find(str2)

#####并查集和set的差异
# 并查集可以实现集合list之间的融合和查找某个值属于哪个集合，set实现不了这一点


