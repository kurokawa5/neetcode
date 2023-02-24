# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
# case 1
#s = "anagram"
#t = "nagaram"
# case 2
s = "rat"
t = "car"

from collections import Counter
print(Counter(s) == Counter(t))