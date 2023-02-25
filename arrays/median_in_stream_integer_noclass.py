import heapq
"""
Created on Wed Feb 20 18:23:04 2019

@author: kanis
"""

'''
	Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
	Examples: 
	[2,3,4] , the median is 3
	[2,3], the median is (2 + 3) / 2 = 2.5
	Design a data structure that supports the following two operations:
	void addNum(int num) - Add a integer number from the data stream to the data structure.
	double findMedian() - Return the median of all elements so far.
	For example:
	addNum(1)
	addNum(2)
	findMedian() -> 1.5
	addNum(3) 
	findMedian() -> 2
'''
max_heap = []
min_heap = [] 

def addNum(num):
    if not max_heap or num > -max_heap[0]:
        heapq.heappush(min_heap, num)
        if len(min_heap) > len(max_heap)+1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        else:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))


def findMedian():
    print(min_heap)
    if len(max_heap) == len(min_heap):
        return (-max_heap[0] + min_heap[0])/2.0
    else:
        return min_heap[0] 


if __name__ == "__main__":
    addNum(1)
    addNum(2)
    print(findMedian())
    addNum(3)
    print(findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
