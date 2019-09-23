def isPalid(x):
    if x<0:
        return False
    s=toString(x)
    i=0
    while i<len(s)-1-i:
        if s[i]!=s[len(s)-1-i]:
            return False
        i=i+1
    return True

def toString(x):
    s=[]
    while x>0:
        s.append(x%10)
        x=x/10
    return s
