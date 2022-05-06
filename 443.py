class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)==0:
            return 0
        pre=chars[0]
        cnt=1
        chars.append("")
        p=0
        for i in range(len(chars)):
            if chars[i]==pre:
                cnt+=1
            else:
                if cnt==1:
                    chars[p]=chars[i]
                    p+=1
                else:
                    strcnt=str(cnt)
                    chars[p]=pre
                    p+=1
                    for v in strcnt:
                        chars[p]=v
                        p+=1
                    pre=chars[i]

        return chars[:p]


