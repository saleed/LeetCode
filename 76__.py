def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s)==0 or len(t)==0 or len(t)>len(s):
        return 0
    dict={}
    for i in t:
        if dict.has_key(i):
            dict[i]=dict[i]+1
        else:
            dict[i]=1

    i=0
    j=0
    si=0
    sj=0
    maxLen=float("inf")
    need=len(t)
    while i<len(s) or j<len(s):
        print need,i,j,s[i:j+1]
        if need>0 and j==len(s):
            break
        elif need>0 and j<len(s):
            if dict.has_key(s[j]) and dict[s[j]]>0:
                need=need-1
                dict[s[j]]=dict[s[j]]-1
            j=j+1
        elif need==0:
            if j-i<maxLen:
                si=i
                sj=j
                maxLen=j-i
            if i<len(s):
                if dict.has_key(s[i]) and dict[s[i]]==0:
                    need=need+1
                    dict[s[i]]=dict[s[i]]+1
                i=i+1
            else:
                break
    return maxLen,si,sj


S = "ADOBECODEBANC"
T = "ABC"
print minWindow(S,T)

