

def reve(l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
nums=[1,2,3,4,5,6,7]
k=3
reve(0,len(nums)-1)
reve(0,k-1)
reve(0,len(nums)-1)
print(nums)