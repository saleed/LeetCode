class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s_ch=""
        for i in s:
            if i!="-":
                if i.isdigit():
                    s_ch+=i
                elif i.isalpha():
                    s_ch+=i.upper()
        div=len(s_ch)/k
        res=""
        res+=s_ch[:len(s_ch)-div*k]
        for i in range(div):
            res+="-"+s_ch[len(s_ch)-div*k+i*k:len(s_ch)-div*k+(i+1)*k]
        if len(res)>0 and res[0]=="-":
            return res[1:]
        return res
s = "5F3Z-2e-9-w"
k=4
a=Solution()
print(a.licenseKeyFormatting(s,k))