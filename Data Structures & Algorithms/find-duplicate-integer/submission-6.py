class Solution:
    # Slow and Fast Pointers
    # Runtime: 56ms
    # Memory: 11.2 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # n is the length of nums.
    def findDuplicate(self, nums: List[int]) -> int:
        slow_1 = 0
        slow_2 = 0
        fast = 0

        while True:
            slow_1 = nums[slow_1]
            fast = nums[nums[fast]]

            if slow_1 == fast:
                # When slow and fast meets up first,
                # then it means that a cycle exists, but
                # it does not mean the first meeting point
                # is the duplicate since it is possible for
                # the slow and fast pointer to meet at the 
                # index of the nums[duplicate].

                while True:
                    # It is a bunch of match why instantiating slow_1
                    # and moving `slow_1` and `slow_2` together will
                    # guarantee it will both reach the duplicate
                    # number.
                    
                    slow_1 = nums[slow_1]
                    slow_2 = nums[slow_2]

                    if slow_1 == slow_2:
                        return slow_1