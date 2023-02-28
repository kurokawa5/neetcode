# 704. Binary Search
# https://leetcode.com/problems/valid-palindrome/
#s = "A man, a plan, a canal: Panama"
s = "c#dc"
newStr = ""
for c in s:
    if c.isalnum():
        newStr += c.lower()

print(True if newStr == newStr[::-1] else False)

"""
s = "a."
s = s.lower()
s = s.replace(" ","")
s = s.replace("@","")
s = s.replace(".","")
s = s.replace(",","")
s = s.replace(":","")

print(s)
if s == s[::-1]:
    print(True)
else:
    print(False)
"""