class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cow=0
        bull=0

        dict={}
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
            else:
                if guess[i] in dict.keys():
                    dict[guess[i]]+=1
                else:
                    dict[guess[i]]=1
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                continue
            if secret[i] in dict.keys():
                cow+=1
                dict[secret[i]]-=1
                if dict[secret[i]]==0:
                    del dict[secret[i]]
        ret=str(bull)+"A"+str(cow)+"B"
        return ret

secret = "1807"
guess = "7810"
a=Solution()
print a.getHint(secret,guess)


secret ="11"
guess = "10"
print a.getHint(secret,guess)
