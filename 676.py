class MagicDictionary(object):

    def __init__(self):

        self.dict={}


    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for v in dictionary:
            self.add(v)


    def add(self,word):
        tmpnode=self
        for v in word:
            if v in tmpnode.dict:
                tmpnode=self.dict[v]
            else:
                tmpnode.dict[v]=MagicDictionary()
                tmpnode=tmpnode.dict[v]
        tmpnode["#"]=1



    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        if len(searchWord)==0:
            return False

        ch=searchWord[0]
        for k in self.dict:
            if k=="#":
                continue
            tmpnode=self.dict[k]
            if k==ch and tmpnode.search(searchWord[1:]):
                return True
            elif k!=ch and tmpnode.puresearch(searchWord[1:]):
                return True
        return False


    def puresearch(self,word):
        tmpnode=self
        for  i in range(len(word)):
            if word[i] in tmpnode.dict:
                tmpnode=tmpnode.dict[word[i]]
            else:
                return False
        if "#" in tmpnode:
            return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
