# only use element once & only one solution exist
nums =[5,9,1,2,4,15,6,3] 
target = 13
def Twosum(nums:list,target:int):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                print(i,j)
                break
Twosum(nums,target)

# using map 
def Twosum_map(nums:list,tar:int):
    n=len(nums)
    hash_map={}
    for i in range(0,n):
        rem = tar-nums[i]
        if rem in hash_map:
            return[hash_map[rem],i]
            
        hash_map[nums[i]]=i    
print(Twosum_map(nums,target))
