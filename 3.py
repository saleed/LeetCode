def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s=="":
        return 0
    s=list(s)
    print(s)
    for l in list(reversed(range(len(s)))):
        i=0
        while(i+l<len(s)):
            print s[i:i+l+1],l
            if len(set(s[i:i+l+1]))==l+1:
                return l+1
            i=i+1




a="abcabcbb"
print lengthOfLongestSubstring(a)



print range(5)
print lengthOfLongestSubstring(" ")
print len(list(" "))
print list(reversed(range(1)))


def lengthOfLongestSubstring2(s):
    """
    :type s: str
    :rtype: int
    """
    if s=="":
        return 0
    maxlen=0
    dic={}
    start=0
    for i in range(len(s)):
        if dic.has_key(s[i]):
            start =max(start,dic[s[i]] +1)#想不通为什么要有max :用例“abbbba
        dic[s[i]] = i
        maxlen=max(i-start+1,maxlen)
    return maxlen



print lengthOfLongestSubstring2(a)
print lengthOfLongestSubstring2("abc")
print lengthOfLongestSubstring2("abcdae")
print lengthOfLongestSubstring2("aaaaa")
print lengthOfLongestSubstring2("ababab")
print lengthOfLongestSubstring2("aab")
print lengthOfLongestSubstring2(" ")

