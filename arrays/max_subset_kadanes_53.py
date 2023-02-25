# Python program to find maximum contiguous subarray 
# def kadane(A):
#     max_current = max_global = A[0] 
#     for i from 1 to length(A) -1 : 
#         max_currentp = max(A[i]. max_current + A[i]) 
#         if max_current > max_global
#             max_global = max_current
#     return max_global 


  
# Function to find the maximum contiguous subarray 
from sys import maxsize 
def maxSubArraySum(a,size): 
       
    max_so_far = -maxsize - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 
   
# Driver function to check the above function  
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print ("Maximum contiguous sum is", maxSubArraySum(a,len(a)))