class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict=[]
        self.followof={}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

        self.dict.append([userId,tweetId])
        if userId not in self.followof.keys():
            self.followof[userId]=set()
            self.followof[userId].add(userId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        count=0
        res=[]
        for ele in self.dict[::-1]:
            if ele[0] in self.followof[userId]:
                count+=1
                res.append(ele[1])
                if count==10:
                    break
        return res



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followof.keys():
            self.followof[followerId]=set()
            self.followof[followerId].add(followerId)
            self.followof[followerId].add(followeeId)
        else:
            self.followof[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followof.keys():
            self.followof[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
#
# a=set()
# a.add()
# a.remove()