

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    #模拟法：超时
    if numRows==1 or len(s)<numRows:
        print(s)
    a=[[' ' for i in range(int(len(s)/2)+numRows-1)] for j in range(numRows)]
    t=0
    r=0
    c=0
    while t<len(s):
        while r<numRows and t<len(s):
            a[r][c]=s[t]
            t=t+1
            r=r+1
        r=numRows-2
        c=c+1
        while r>=0 and t<len(s):
            a[r][c]=s[t]
            r=r-1
            c=c+1
            t=t+1
        c=c-1
        r=1
        b=""
    # for i in range(numRows):
    #     print a[i]
    for i in range(numRows):
        for j in range(int(len(s)/2)+numRows-1):
            if a[i][j]!= ' ':
                b+=a[i][j]
    return b


    #推倒公式，利用字段出现的周期性


test="f1273784"

test2="oxjpkcpdekyazevyzxudsirvddoxmptaodryfhdltcmuijsigolaxevcimbwduwrzqrhxvssxgmhpgpxvdyujvwrhzpktmdvcvcbquvpbhwsposktsecncwxbljxznsdiugaqbprknmabekwwrzltxixiuwihonrkutaviuixgibkuxinythvcgewcofsbycxrctbydyelzqhzyvxsetwkzuonbgqziosmjvnmtrzvkiuidrcjkavlwjaxrrybhsqsndghwhegpyrvrvgcwcpsnqsfjqgqjykwbqfyzjeojxlbtsfpwujjkbqtuzldxxbznjxmuddedqhwioneiwqvygqufezdbacrlbfggkmjbvfjjsqtrgormhlulkxombfyengkxuwypdkyyarpiiiwptqcdnsrqypunxfkrdlggvggxaxhifdzyuddjvvcvkwikdvbggkpbqvyqvfaakzzgecsazuxmqgwwbxchhtkarkqmrrmbsnixsczrwwdoebkfzpoikyibkbpbuedmrnllpkfnjkbnmovnfjxpkitwjiydmdrgqdthpywyjzmvnhksshkepdbylbdaexiwabfrabqlaegqnskhzumpzpplqvnwsvsuwxlyabjchruujhclbqcbhtozobviypcwmoxoriqbanvluzyxpaawwovkrsvrhxotnnjhvcivpfjjfjgwkhtgxqsrjpiqnymclvlhxveobpxgzgclnxtmqndzdmrsmduybifadlpebomaurljoewerzfwnxoacjydrfeuqvbtjnteegnvmjbgljcygraicamvfspynsrwgnamvqjiblomuqlcjnkloygvsytfqneycglxwwfyhtkdmxhvlujbspwlnqsefwchdpezmmzvfkbtjirwcaxxpukfmcltznaefgdtsdqaprvacmxemubeoljcquvpjxvqeajwfcyutuvvgscv"

convert(test,3)
#
# a = [[i for i in range(3)] for j in range(6)]
#
#
# print a
# print a[5][1]

