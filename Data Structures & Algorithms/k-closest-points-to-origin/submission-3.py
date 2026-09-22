import heapq

from math import sqrt

class Solution:
    """
    Min Heap
    Runtime: 30ms
    Memory: 8.5 MB
    Time Complexity: O(n)
    Space Complexity: O(n)
    n is the length of `points`.
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_distances = []

        for point in points:
            x_i = point[0]
            y_i = point[1]
            euclidean_distance = sqrt((x_i - 0)**2 + (y_i - 0)**2)
            euclidean_distances.append((euclidean_distance, [x_i, y_i]))

        k_closests_points = []
        heapq.heapify(euclidean_distances)

        for i in range(k):
            k_closests_points.append(heapq.heappop(euclidean_distances)[1])

        return k_closests_points