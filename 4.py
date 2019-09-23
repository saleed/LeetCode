def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    newl=[]
    id1=0
    id2=0
    while id1<len(nums1) or id2<(nums2):
        if id1==len(nums1) and id2==len(nums2):
            print newl
            if len(newl)%2:
                return newl[len(newl)/2]
            else:
                return (newl[len(newl)/2]+newl[len(newl)/2-1])/2.0
        elif id1==len(nums1):
            newl.append(nums2[id2])
            id2=id2+1
        elif id2==len(nums2):
            newl.append(nums1[id1])
            id1=id1+1
        else:
            if nums1[id1]<nums2[id2]:
                newl.append(nums1[id1])
                id1=id1+1
            else:
                newl.append(nums2[id2])
                id2 = id2 + 1




a=[1,2]
b=[3,4]

print findMedianSortedArrays(a,b)
