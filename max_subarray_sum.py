nums = [-2,1,-3,4,-1,2,1,-5,4]
def subarr_sum(nums:list):
    n = len(nums)
    max_sum = 0
    for i in range(0,n):
        total=0
        for j in range(i,n):
            total+=nums[j]
            max_sum =max(max_sum,total)
    return max_sum

print(subarr_sum(nums))

def max_subarr_sum(nums:list):
    n = len(nums)
    max_sum =float("-inf")
    sum = 0
    for i in range(0,n):
        sum += nums[i]
        max_sum = max(max_sum,sum)
        if sum < 0:
            sum = 0
    return max_sum

print(max_subarr_sum(nums))