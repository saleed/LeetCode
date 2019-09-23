import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        visited = []
        heap = []
        output = []

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.append((0, 0))

        while len(output) < k and heap:

            val = heapq.heappop(heap)
            output.append((nums1[val[1]], nums2[val[2]]))

            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heapq.heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
                visited.append((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heapq.heappush(heap, (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))
                visited.append((val[1], val[2] + 1))

        return output
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
a=Solution()
print(a.kSmallestPairs(nums1,nums2,k))

#
# consider two input arrays:
# nums1=[a1,a2,a3]
# nums2=[b1,b2,b3]
#
# and let's say k=3
#
# We know the brutal force way to do it is to calc (a1, b1), (a1, b2), (a1,b3)....(a3,b3)'s
# sum respectively and sort the sums,
# and pick the top 3 of them. This algorithm is O(n2). And we need an algorithm better than that.
#
# So, the overall idea of the algorithm:
# Maintain a min-heap to keep only part of the
#  whole set of combinations of all elements from nums1 and nums2.
# That way, we can avoid the brutal force way which is O(n2).
# We only push necessary pairs into the heap, until we find all of the k pairs.
#
# How we achieve that (for the sake of explanation, ignore the corner cases for now):
# 1, create a heap, then push (S0, N1, N2) into the heap,
# where N1 is the position of first element in nums1, N2 is the position of first element in nums2,
#  S0 is the sum of N1 and N2. Mark (N1,N2) as visited.
# 2, Pop the root element (S0, N1,N2) out of the heap, add (N1,N2) to the result to be returned.
# and immediately push (S1, N1+1,N2) and (S2, N1, N2+1) into the heap,
# where S1 = nums1[N1+1]+nums2[N2], S2 = nums1[N1] + nums2[N2+1].
# Here, if a pair (Nx, Ny) has already been visited, we'll ignore it and not push it to the heap.
# 3, repeat this, until all k pairs have been added into the return list. Return the list.

