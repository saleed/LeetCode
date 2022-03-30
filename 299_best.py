class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        sset=set(secret)
        rset=set(guess)

        bull=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1

        return str(bull)+"A"+str(len(sset.intersection(rset)))+"B"