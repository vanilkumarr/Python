m=int(input("enter how many numbers you want"))
nums=[int(input()) for i in range(m)]
n=len(nums)
for i in range(n):
    min1=i
    for j in range(i+1,n):
        if nums[min1] > nums[j]:
            min1=j
    if min1 !=i:
        nums[i],nums[min1] = nums[min1],nums[i]
print(nums)
        