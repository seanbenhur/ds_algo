"""Given a string lowercase alphabet s, eliminate consecutive duplicate characters from the string and return it.

That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "aaaaaabbbccccaaaaddf"
Output
"abcadf"
Example 2
Input
s = "a"
Output
"a"""


from collections import Counter

s = "aaaaaabbbccccaaaaddf"
l = [s[0]]

for c in s[1:]:
    if c == l[-1]:
        print(l[-1])
        continue 
    else:
        l.append(c)



print(l)