hist = {}

nums = 
for i, n in enumerate(nums):
    if target - n in hist:
        return [hist[target-n], i]
    hist[n] = i
    
    
    
