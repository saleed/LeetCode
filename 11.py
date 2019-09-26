#从序列头到序列尾，
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0
    p = 0
    q = len(height) - 1
    while p < q:
        a = (q - p) * min(height[p], height[q])
        if area < a:
            area = a
        if height[p] < height[q]:
            p = p + 1
        else:
            q = q - 1
    return area
