from math import sqrt

class Solution:
    """
    Brute Force
    Runtime: 32ms
    Memory: 8.5 MB
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    n is the length of `points`.
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distance = []

        for point in points:
            x_i = point[0]
            y_i = point[1]
            euclidean_distance = sqrt((x_i - 0)**2 + (y_i - 0)**2)
            points_distance.append((euclidean_distance, [x_i, y_i]))

        points_distance.sort()
        k_closest = []

        for i in range(k):
            k_closest.append(points_distance[i][1])

        return k_closest