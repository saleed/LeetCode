def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    if len(s1)+len(s2)!=len(s3):
        return False
    return dfs(s1,s2,s3,0,0)



def dfs(s1,s2,s3,id1,id2):
    flag1=flag2=False
    # if id1==len(s1) and id2==len(s2):
    #     return True
    # elif id1==len(s1) and id2!=len(s2):
    #     id3=id1-1+id2
    # elif id1!=len(s1) and id2==len(s2):
    #     id3=id2-1+id1
    # else:
    #     id3=id1+id2
    if id1==len(s1) and id2==len(s2):
        return True
    id3=id1+id2


    if id1<len(s1) and s3[id3]==s1[id1]:
        flag1=dfs(s1,s2,s3,id1+1,id2)
    if id2<len(s2) and s3[id3]==s2[id2]:
        flag2=dfs(s1,s2,s3,id1,id2+1)
    if flag1 or flag2:
        return True
    return False





s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

print isInterleave(s1,s2,s3)







s1 = "a"
s2 = "b"
s3 = "ab"

print isInterleave(s1,s2,s3)
