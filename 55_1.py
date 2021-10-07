##比较常见的想法是建模为一个广度优先遍历，复杂度O(n2) 但是这种情况会明显处超时，需要剪枝
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.bfs2(nums)



    ##相比bfs，减少了队列中的重复节点，
    def bfs2(self,nums):
        if len(nums)==0:
            return False
        vis=set()
        queue=[0]
        while len(queue)>0:
            tmp_node=queue[0]
            queue=queue[1:]
            if tmp_node == len(nums) - 1:
                return True
            for i in range(tmp_node+1,tmp_node+nums[tmp_node]+1):
                if i not in vis:
                    queue.append(i)
                    vis.add(i)
        return False


    def bfs(self,nums):
        if len(nums)==0:
            return False
        queue=[0]
        while len(queue)>0:
            tmp_node=queue[0]
            queue=queue[1:]
            for i in range(tmp_node+1,tmp_node+nums[tmp_node]+1):
                if i==len(nums)-1:
                    return True
                queue.append(i)
        return False






