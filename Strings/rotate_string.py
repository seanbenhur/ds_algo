"""We are given two strings, s and goal.

A shift on s consists of taking string s and moving the leftmost character to the rightmost position. For example, if s = 'abcde', then it will be 'bcdea' after one shift on s. Return true if and only if s can become goal after some number of shifts on s."""




def rotate_string(s,t):
    if len(s)!=len(goal):
        return False
    return s in t+t

s = input()
t = input()
print(rotate_string(s,t))