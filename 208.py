class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic=[None]*27
        self.val=1

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p=self
        for i in range(len(word)):
            if p.dic[ord(word[i])-ord('a')]!=None: #be careful for this is very important
                p=p.dic[ord(word[i]) - ord('a')]
            else:
                newTrie=Trie()
                p.dic[ord(word[i])-ord('a')]=newTriexx
                p=newTrie
        p.dic[26]=Trie()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p=self
        for i in range(len(word)):
            if p.dic[ord(word[i])-ord('a')]!=None:
                p=p.dic[ord(word[i])-ord('a')]
            else:
                return False
        if p.dic[26]!=None:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p=self
        for i in range(len(prefix)):
            if p.dic[ord(prefix[i])-ord('a')]!=None:
                p=p.dic[ord(prefix[i])-ord('a')]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
[[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
[null,null,null,null,null,null,null,false,false,false,false,false,false,false,true,true,false,false,true,false,false,false,true,true,true]
[null,null,null,null,null,null,null,false,true,false,false,false,false,false,true,true,false,true,true,false,false,false,true,true,true]