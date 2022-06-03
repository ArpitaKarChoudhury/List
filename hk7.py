#  You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.
#  Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]

s = "bar foo the foo bar man"
words = "foo bar"
a=s.split()
print(a)
c=0
while c<len(a):
    if words[c]!=a[c]:
        print(c,end=" ")
    c=c+1