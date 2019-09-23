def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    if n==1:
        return [[1]]
    mtx = [[0 for i in range(n)] for j in range(n)]
    i = 0
    j = -1
    count=0
    while count <n*n:
        while j + 1 < n and mtx[i][j + 1] == 0:
            count = count + 1
            mtx[i][j + 1] = count
            j = j + 1
        while i + 1 < n and mtx[i + 1][j] == 0:
            count = count + 1
            mtx[i + 1][j] = count
            i = i + 1
        while j - 1 >= 0 and mtx[i][j - 1] == 0:
            count = count + 1
            mtx[i][j - 1] = count
            j = j - 1
        while i - 1 >= 0 and mtx[i - 1][j] == 0:
            count = count + 1
            mtx[i - 1][j] = count
            i = i - 1

    # print mtx
    return mtx

print(generateMatrix(3))