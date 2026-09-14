nums = [3,4,0,1]
n=len(nums)
for i in range(0,n):
    if i not in nums:
        print(i)
        break

def missing_no(nums:list)->int:
    n=len(nums)
    return (n*(n+1))//2 - sum(nums)

print(missing_no(nums))
