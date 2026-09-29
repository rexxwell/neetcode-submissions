import heapq
from collections import defaultdict


class Twitter:
    """
    Min Heap, Hash Maps, and Sets (Optimized)
    Runtime: 62ms
    Memory: 11.4 MB
    Time Complexity: O(k + 10logk)
    Space Complexity: O(n^2 + n + m) = O(n^2 + m)
    n is the number of users.
    m is the number of tweets.
    k is the number of users the user `userId` follows. (k <= n)
    """

    def __init__(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(n^2 + n + m)
        n is the number of users.
        m is the number of tweets.
        """

        self.user_followees = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.tweet_number = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Time Complexity: O(1)* average, O(n) worst case
        Space Complexity: O(1)
        n is the number of users.
        """

        self.tweet_number += 1
        self.user_tweets[userId].append((-self.tweet_number, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Time Complexity: O(k + k + 10logk) = O(k + 10logk)
        Space Complexity: O(k + 10) = O(k)
        k is the number of users the user `userId` follows. (k <= n)
        """

        tweets = []
        recent_tweets = []

        for user_id in self.user_followees.get(userId, set()) | {userId}:
            user_id_tweets = self.user_tweets.get(user_id, list())

            if user_id_tweets:
                tweets.append(user_id_tweets[-1] + (user_id, len(user_id_tweets) - 1))

        heapq.heapify(tweets)

        while tweets and len(recent_tweets) < 10:
            _tweet_number, _tweet_id, user_id, index = heapq.heappop(tweets)
            recent_tweets.append(_tweet_id)

            if index - 1 >= 0:
                heapq.heappush(tweets, self.user_tweets[user_id][index - 1] + (user_id, index - 1))

        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Time Complexity: O(1)* average, O(n) worst case
        Space Complexity: O(1)
        n is the number of users.
        """

        if followerId != followeeId:
            self.user_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Time Complexity: O(1)* average, O(n) worst case
        Space Complexity: O(1)
        n is the number of users.
        """

        if followerId != followeeId:
            self.user_followees[followerId].discard(followeeId)