# https: // www.geeksforgeeks.org/find-k-closest-points-to-the-origin/
# https://leetcode.com/problems/k-closest-points-to-origin/

# https: // docs.python.org/3/howto/sorting.html

def pClosest(points, K):

	points.sort(key=lambda x: x[0]**2 + x[1]**2)

	return points[:K]


# Driver program
points = [[3, 3], [5, -1], [-2, 4]]

K = 2

print(pClosest(points, K))


# a = [(1, 2), (4, 1), (9, 10), (13, -3)]
# a.sort(key=lambda x: x[1])

# print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
