from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        self.follow(userId, userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for user, tweet in reversed(self.tweets):
            if user in self.following[userId]:
                res.append(tweet)
                if len(res) == 10:
                    break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
