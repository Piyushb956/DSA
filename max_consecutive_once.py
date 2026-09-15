nums = [1,1,0,1,0,1,0,0,1,1,1,1]

def max_consecutive_once(nums:list):
    count,max_count=0,0
    for num in nums :
        if num ==1:
            count+=1
        else: 
            max_count = max(max_count,count)
            count = 0
    return max(max_count,count)

print(max_consecutive_once(nums))