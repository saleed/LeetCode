class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        return word.lower()==word or word[1:].lower()==word or word.upper()==word