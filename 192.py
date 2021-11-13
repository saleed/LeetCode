# Read from the file words.txt and output the word frequency list to stdout.
def cmp(a,b):
    return a[1]>a[0]
f=open("words.txt")
freq={}
for line in f.readlines():
    sp=line.split(" ")
    for v in sp:
        if v!="" :
            if v in freq:
                freq[v]+=1
            else:
                freq[v]=1

freqList=[]
for k in freq:
    freqList.append([k,freq[k]])
freqList.sort(key=cmp)

