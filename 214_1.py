class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mid=len(s)/2

        lstr=str(s[:mid][::-1])
        rstr=s[mid+1:]
        midchar=s[mid]
        res=s[1:][::-1]+s
        while len(lstr)>0:
            print(lstr,midchar,rstr)
            if len(lstr)<=len(rstr):
                if rstr[:len(lstr)]==lstr and 2*len(rstr)-1<len(res):
                    res=rstr[::-1]+midchar+rstr
                    print(2,res)
                    break



            rstr=midchar+rstr
            midchar=lstr[0]
            lstr=lstr[1:]

        lstr = s[:mid][::-1]
        rstr = s[mid:]
        while len(lstr)>0:
            print(lstr,rstr)
            if len(lstr)<=len(rstr):
                if rstr[:len(lstr)]==lstr and 2*len(rstr)<len(res):
                    print(1)
                    res=rstr[::-1]+rstr
                    break

            rstr=lstr[0]+rstr
            lstr=lstr[1:]
        return res



a="aacecaaa"
s=Solution()
print(s.shortestPalindrome(a))





