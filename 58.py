def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    s=rmv(s)
    arr=s.split(" ")
    return len(arr)





def rmv(s):
    i=0
    j=0
    for i in range(len(s)):
        if s[i]!=' ':
            break
    for j in list(reversed(range(len(s)))):
        if s[j]!=' ':
            break
    if i>j:
        return ""
    return s[i:j+1]


s1="12kjf 902392 0239023"

print s1.split(" ")

s2="a    bsdfa"
print s2.split(" ")
s3=""
print s3.split(" ")
print rmv(s3)

