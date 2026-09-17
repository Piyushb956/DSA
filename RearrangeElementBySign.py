nums = [5,10,-3,-1,-10,6]

# brute force, TC= O(n+n/2),SC= O(N)
def arrangeSign(nums:list)->list:
    pos= []
    neg= []
    for num in nums :
        if num >=0:
            pos.append(num)
        else :
            neg.append(num)

    for i in range(0,len(pos)):
        nums[2*i] = pos[i]
        nums[2*i+1] = neg[i]
    
    return nums

print(arrangeSign(nums))

def arrangeElement(nums : list)->list:
    res = [0]*len(nums)
    pos = 0
    neg =1
    for num in nums:
        if num >=0:
            res[pos]=num
            pos +=2
        else :
            res[neg]=num
            neg += 2
    
    
    return res

print(arrangeElement(nums))