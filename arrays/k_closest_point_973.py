# https: // www.geeksforgeeks.org/find-k-closest-points-to-the-origin/
# https://leetcode.com/problems/k-closest-points-to-origin/


def pClosest(points, K):

	points.sort(key=lambda K: K[0]**2 + K[1]**2)

	return points[:K]


# Driver program
points = [[3, 3], [5, -1], [-2, 4]]

K = 2

print(pClosest(points, K))
