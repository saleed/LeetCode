class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        st=[]
        while x:
            st.append(x%10)
            x/=10
        p=0
        q=len(st)-1
        while p<q:
            if st[p]!=st[q]:
                return False
            p+=1
            q-=1
        return True


