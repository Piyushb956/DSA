inums = [3,4,2,0,1,6]
n=len(nums)
# brute force
for i in range(0,n):
    if i not in nums:
        print(i)
        break
# missing no = diff in sum of len of list and sum of element
def missing_no(nums:list)->int:
    n=len(nums)
    # o(n)
    return (n*(n+1))//2 - sum(nums) 
print(missing_no(nums))

def  missing_no_2(nums:list)->int:
    frq = {}
    n =len(nums)
    for i in range(0,n+1):
        frq[i]=0
    for num in nums:
        frq[num]=1
    for k,v in frq.items():
        if v==0:
            return k

print(missing_no_2(nums))
