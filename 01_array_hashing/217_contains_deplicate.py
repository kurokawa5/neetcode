# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/
nums = [1,2,3,1]
#nums = [1,2,3,4]
#nums = [1,1,1,3,3,4,3,2,4,2]

if len(nums) != len(set(nums)):
    print(True)
else:
    print(False)