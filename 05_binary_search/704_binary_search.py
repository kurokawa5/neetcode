# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/
# import sys
nums = [-1,0,3,5,9,12]
target = 9

# Set the left and right boundaries
left = 0
right = len(nums) - 1

# Under this condition
while left <= right:
    #mid = (left + right) // 2
    mid = left + ((right - left) // 2)
    # Case 1, return the middle index.
    if nums[mid] == target:
        print(mid)
        break
    # Case 2, discard the smaller half.
    elif nums[mid] < target:
        left = mid + 1
    # Case 3, discard the larger half.
    else:
        right = mid - 1
# If we finish the search without finding target, return -1.
print(-1)
