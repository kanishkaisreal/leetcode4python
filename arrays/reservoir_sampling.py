# this is a common question at Facebook and Google. 
# https: // www.dailycodingproblem.com/blog/how-to-pick-a-random-element-from-an-infinite-stream/

# An efficient Python3 program to randomly select k items
#  from a stream of items
import random
# A utility function to print an array


# def printArray(stream, n):
# 	for i in range(n):
# 		print(stream[i], end=" ")
# 	print()

# A function to randomly select k items from stream[0..n-1].


# def selectKItems(stream, n, k):
# 	i = 0
# 		# index for elements in stream[]reservoir[] is the output
# 		# array. Initialize it with  first k elements from stream[]
# 	reservoir = [0]*k
# 	for i in range(k):
# 		reservoir[i] = stream[i]

# 		# Iterate from the (k+1)th element to nth element
# 	while(i < n):
# 		# Pick a random index  from 0 to i.
# 		j = random.randrange(i+1)

# 			# If the randomly picked index is smaller than k,
# 			# then replace the element  present at the index
# 			# with new element from stream
# 		if(j < k):
# 			reservoir[j] = stream[i]
# 		i += 1

# 	print("Following are k randomly selected items")
# 	printArray(reservoir, k)


def pick_random(big_stream):
    random_element = None
    for i, e in enumerate(big_stream):
        print(i,e)
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    print(random_element)


stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k = 2
pick_random(stream)
n = len(stream)
k = 5
# selectKItems(stream, n, k)
