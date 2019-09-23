class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # preorder=preorder.split(',')
        # if len(preorder)==0:
        #     return True
        # if preorder[0]=="#":
        #     return False
        # st=[]
        # p=0
        # while p<len(preorder):
        #     print(st)
        #     if preorder
        #     while p<len(preorder) and preorder[p]!='#':
        #         st.append(preorder[p])
        #         p+=1
        #     if p==len(preorder) or preorder[p]!='#':
        #         return False
        #     if p+1<len(preorder):
        #         p+=1
        #         st.pop()
        #     else:
        #         return False
        # if len(st)>0:
        #     return False
        # return True


a=Solution()

t="9,3,4,#,#,1,#,#,2,#,6,#,#"

print(a.isValidSerialization(t))