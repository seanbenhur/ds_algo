"Check whether  given two strings are palindrome"



from collections import Counter

#using counter
def check_palindrome(s,t):
    return Counter(s)==Counter(t)

#using sort
def check_palindrome_sort(s,t):
    return sorted(s)==sorted(t)



if __name__ == "__main__":
    s, t = input(), input()
    print("Using  Counter")
    print(check_palindrome(s,t))
    print("Using  Sorted")
    print(check_palindrome_sort(s,t))