import heapq


class Twitter:
    """
    Min Heap and Hash Maps
    Runtime: 405ms
    Memory: 11.2 MB
    Time Complexity: O(n + m)
    Space Complexity: O(n^2 + n + m) = O(n^2 + m)
    n is the number of users using Twitter.
    m is the number of posts in Twitter.
    """

    def __init__(self):
        self.user_tweets = {}
        self.user_followers = {}
        self.number_of_recent_tweets = 10
        self.post_number = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_number += 1
        if userId in self.user_tweets:
            self.user_tweets[userId].append((-self.post_number, tweetId))
        else:
            self.user_tweets[userId] = [(-self.post_number, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        recent_tweets = []

        for followeeId in self.user_followers.get(userId, []):
            for tweet in self.user_tweets.get(followeeId, []):
                tweets.append(tweet)
        
        for tweet in self.user_tweets.get(userId, []):
            tweets.append(tweet)
        
        heapq.heapify(tweets)

        for i in range(len(tweets) if len(tweets) <= self.number_of_recent_tweets else self.number_of_recent_tweets):
            date_and_time, tweedId = heapq.heappop(tweets)
            recent_tweets.append(tweedId)

        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.user_followers:
                if followeeId not in self.user_followers[followerId]:
                    self.user_followers[followerId].append(followeeId)
            else:
                self.user_followers[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.user_followers:
                if followeeId in self.user_followers[followerId]:
                    self.user_followers[followerId].remove(followeeId)
        
