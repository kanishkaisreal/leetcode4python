# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 
# https: // www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/

# Daily Coding Problem: Problem  # 47 [Easy]

# Case 1 : when k  = 1   ( only one transaction is allowed )

# https: // www.geeksforgeeks.org/maximum-difference-between-two-elements/
#  maximum difference between two elements such that larger element appears after the smaller number 

 # time complexity for this implementation  O(n) 
def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
    min_array_element, max_array_element = arr[0], arr[1]

    for i in range(1, arr_size):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
            max_array_element = arr[i] 
            min_array_element = min_element 


        if (arr[i] < min_element):
            min_element = arr[i]
            min_element
    return max_diff, max_array_element, min_array_element


# Driver program to test above function
# arr = [2,3,10, 6, 4, 8, 1]
arr = [7, 9, 5, 6, 3, 2]
size = len(arr)
max_diff, max_array_element, min_array_element = maxDiff(arr, size)
print("Maximum difference is %d, between %d and %d" %(max_diff, max_array_element, min_array_element))

# f"Maximum difference is {max_diff}, between {max_array_element} and {min_array_element}"
