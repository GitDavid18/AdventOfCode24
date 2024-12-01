file1 = open("01/input.txt", "r")
fileContent = file1.readlines()
nums1 = []
nums2 = []

for row in fileContent:
    nums = row.split()
    nums1.append(int(nums[0]))
    nums2.append(int(nums[1]))

nums1.sort()
nums2.sort()

sum = 0

print("len of nums1:" + str(len(nums1)))
print("len of nums2:" + str(len(nums2)))

for i in range(len(nums1)):
    sum += abs(nums1[i] - nums2[i])
print("the sum is " + str(sum))    
        
overall_similarity = 0       
for i in range(len(nums1)):
    similarity = 0
    for k in range(len(nums2)):
        if (nums1[i] == nums2[k]):
            similarity += 1
        
    overall_similarity += similarity * nums1[i]
    
print("The similarity is " + str(overall_similarity))    
        