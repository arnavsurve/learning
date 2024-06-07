nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

intersection = []

for i in nums1:
    if i in nums2 and i not in intersection:
        intersection.append(i)

print(intersection)
