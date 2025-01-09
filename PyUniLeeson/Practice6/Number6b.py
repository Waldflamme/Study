#6b
cort1 = (1,2,3,4,5,6)
cort2 = (4,5,6,7,8,9)
nums = []
for i in range(len(cort1)):
        nums.append(cort1[i])
for j in range(len(cort2)):
    if cort2[j] not in cort1:
        nums.append(cort2[j])
print(cort1)
print(cort2)
print(tuple(nums))