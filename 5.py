
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    s=list(s)
    for l in reversed(range(len(s))):
        for start in range(len(s)):
            # print start,l
            if start+l<len(s) and isPalid(s[start:start+l+1]):
                return str(s[start:start+l+1])

def isPalid(s):
    i=0
    while i<len(s)-1-i:
        if s[i]!=s[len(s)-1-i]:
            return 0
        i=i+1
    return 1

t1="abbba"
t2="abac"
print longestPalindrome(t1)
print longestPalindrome(t2)
print isPalid(t1)