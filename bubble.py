m=int(input("enter how many numbers you want"))
nums=[int(input()) for i in range(m)]
for j in range(len(nums)-1):
    for i in range(len(nums)-1-j):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
        else:
            print(nums)

print(nums)

