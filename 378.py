# For n X n matrix,
#
#
# The time complexity is O(n * log(n) * log(N)), where N is the search space that ranges from the smallest element to the biggest element. You can argue that int implies N = 2^32, so log(N) is constant. In a way, this is an O(n * log(n)) solution.
#
# The space complexity is constant.
#
# I thought this idea was weird for a while. Then I noticed the previous problem 377. Combination Sum IV is pretty much doing the same thing, so this idea may actually be intended.
#
# Here is a 8-liner implementation:
#
# class Solution(object):
#     def kthSmallest(self, matrix, k):
#         lo, hi = matrix[0][0], matrix[-1][-1]
#         while lo<hi:
#             mid = (lo+hi)//2
#             if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
#                 lo = mid+1
#             else:
#                 hi = mid
#         return lo
# 2. Heap solution gives me 176 ms. The time complexity is O(k * log n), so the worst-case and average-case time complexity is O(n^2 * log n). Space complexity is O(n).
#
# class Solution(object):
#     def kthSmallest(self, matrix, k):
#         heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
#         heapq.heapify(heap)
#         ret = 0
#         for _ in range(k):
#             ret, i, j = heapq.heappop(heap)
#             if j+1 < len(matrix[0]):
#                 heapq.heappush(heap, (matrix[i][j+1], i, j+1))
#         return ret
# 3. Sorting gives me 80ms. Time complexity of sorting an array of size n^2 is O(n^2 * log n). Space complexity is O(n^2).
#
# The difference is that Timsort implemented in Python is capable of taking advantage of existing partial orderings. Moving sorted data in bulk is always faster than comparing and moving individual data elements, due to modern hardware architecture. Time complexity is the same because merging n sorted arrays of size n is still O(n^2 * log n) in the worst case.
#
# class Solution(object):
#     def kthSmallest(self, matrix, k):
#         l = []
#         for row in matrix:
#             l += row
#         return sorted(l)[k-1]
# Here are some O(n^3) (slow due to list concatenation) 1-liners:

# class Solution(object):
#     def kthSmallest(self, matrix, k):
#         return sorted(sum(matrix, []))[k-1]
# and

# class Solution(object):
#     def kthSmallest(self, matrix, k):
#         return sorted(reduce(lambda a,b:a+b, matrix))[k-1]
# # # Here are some O(n^2 * log n) 1-liners provided by @StefanPochmann
#
#     return sorted(itertools.chain(*matrix))[k-1]
#     return sorted(a for row in matrix for a in row)[k-1]
#     return sorted(itertools.chain.from_iterable(matrix))[k-1]

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [(matrix[0][0],0,0)]
        # print(heap
        heapq.heapify(heap)
        count=0
        ret=0
        while count<k:
            ret, i, j = heapq.heappop(heap)
            # print(ret
            if j+1 < len(matrix[0]) and (matrix[i][j+1],i,j+1)not in heap:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
            if i+1<len(matrix) and (matrix[i+1][j],i+1,j) not in heap:
                heapq.heappush(heap,(matrix[i+1][j],i+1,j))
            count+=1
        return ret


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
a=Solution()
print(a.kthSmallest(matrix,8))

matrix=[[1,3,5],[6,7,12],[11,14,14]]
k=6
print(a.kthSmallest(matrix,k))

test=[(0,0),(1,2),(3,4)]
heapq.heapify(test)
heapq.heappush(test,(5,6))
print((1,3) in test)

