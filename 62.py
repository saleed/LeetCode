def uniquePaths( m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    dp=findPaht2(m,n)
    return dp[m-1][n-1]





#
# #
# def findPath(i,j,m,n,count):
#     print i,j
#     if i==m-1 and j==n-1:
#         count.append(1)
#         return
#     if i==m-1:
#         findPath(i,j+1,m,n,count)
#         return
#     if j==n-1:
#         findPath(i+1,j,m,n,count)
#         return
#     findPath(i+1,j,m,n,count)
#     findPath(i,j+1,m,n,count)
#     return



def findPaht2(m,n):
    dp=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j]=1
            elif i==0:
                dp[i][j]=dp[i][j-1]
            elif j==0:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp




print uniquePaths(3,2)



# def test(a,n):
#     if n<2:
#         test(a,n+1)
#         return
#     print id(a)
#     print a
#
# a=3
# print id(a)
# print test(a)
