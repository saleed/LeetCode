class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res=[]
        self.dfs(word,0,"",res)
        self.dfs(word,1,"",res)

        res.sort()
        return res

    def dfs(self,word,flag,tmp,res):
        if len(word)==0:
            res.append(tmp[:])
            return
        for i in range(len(word)):
            if flag==0:
                tmp+=str(i+1)
                self.dfs(word[i+1:],1,tmp,res)
                tmp=tmp[:len(tmp)-len(str(i+1))]
            else:
                tmp+=word[:i+1]
                self.dfs(word[i+1:],0,tmp,res)
                tmp=tmp[:len(tmp)-(i+1)]


a=["10n","111","1n1e1a1t1o1","1n1e1a1t1on","1n1e1a1t2n","1n1e1a1t3","1n1e1a1ti1n","1n1e1a1ti2","1n1e1a1tio1","1n1e1a1tion","1n1e1a2i1n","1n1e1a2i2","1n1e1a2io1","1n1e1a2ion","1n1e1a3o1","1n1e1a3on","1n1e1a4n","1n1e1a5","1n1e1ac1i1n","1n1e1ac1i2","1n1e1ac1io1","1n1e1ac1ion","1n1e1ac2o1","1n1e1ac2on","1n1e1ac3n","1n1e1ac4","1n1e1act1o1","1n1e1act1on","1n1e1act2n","1n1e1act3","1n1e1acti1n","1n1e1acti2","1n1e1actio1","1n1e1action","1n1e2c1i1n","1n1e2c1i2","1n1e2c1io1","1n1e2c1ion","1n1e2c2o1","1n1e2c2on","1n1e2c3n","1n1e2c4","1n1e2ct1o1","1n1e2ct1on","1n1e2ct2n","1n1e2ct3","1n1e2cti1n","1n1e2cti2","1n1e2ctio1","1n1e2ction","1n1e3t1o1","1n1e3t1on","1n1e3t2n","1n1e3t3","1n1e3ti1n","1n1e3ti2","1n1e3tio1","1n1e3tion","1n1e4i1n","1n1e4i2","1n1e4io1","1n1e4ion","1n1e5o1","1n1e5on","1n1e6n","1n1e7","1n1er1c1i1n","1n1er1c1i2","1n1er1c1io1","1n1er1c1ion","1n1er1c2o1","1n1er1c2on","1n1er1c3n","1n1er1c4","1n1er1ct1o1","1n1er1ct1on","1n1er1ct2n","1n1er1ct3","1n1er1cti1n","1n1er1cti2","1n1er1ctio1","1n1e...
b=["11","10n","9o1","9on","8i2","8i1n","8io1","8ion","7t3","7t2n","7t1o1","7t1on","7ti2","7ti1n","7tio1","7tion","6c4","6c3n","6c2o1","6c2on","6c1i2","6c1i1n","6c1io1","6c1ion","6ct3","6ct2n","6ct1o1","6ct1on","6cti2","6cti1n","6ctio1","6ction","5a5","5a4n","5a3o1","5a3on","5a2i2","5a2i1n","5a2io1","5a2ion","5a1t3","5a1t2n","5a1t1o1","5a1t1on","5a1ti2","5a1ti1n","5a1tio1","5a1tion","5ac4","5ac3n","5ac2o1","5ac2on","5ac1i2","5ac1i1n","5ac1io1","5ac1ion","5act3","5act2n","5act1o1","5act1on","5acti2","5acti1n","5actio1","5action","4r6","4r5n","4r4o1","4r4on","4r3i2","4r3i1n","4r3io1","4r3ion","4r2t3","4r2t2n","4r2t1o1","4r2t1on","4r2ti2","4r2ti1n","4r2tio1","4r2tion","4r1c4","4r1c3n","4r1c2o1","4r1c2on","4r1c1i2","4r1c1i1n","4r1c1io1","4r1c1ion","4r1ct3","4r1ct2n","4r1ct1o1","4r1ct1on","4r1cti2","4r1cti1n","4r1ctio1","4r1ction","4ra5","4ra4n","4ra3o1","4ra3on","4ra2i2","4ra2i1n","4ra2io1","4ra2ion","4ra1t3","4ra1t2n","4ra1t1o1","4ra1t1on","4ra1ti2","4ra1ti1n","4ra1tio1","4ra1tion","4rac4","...
b.sort()
print(a)
print(b)