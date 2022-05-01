"""Given a roman numeral, convert it to an integer."""

def roman_to_int(s):
    _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    prev = 0
    res = 0
    for i in reversed(s):
        if _dict[i]>=prev:
            res += _dict[i]
        else:
            res -= _dict[i]
        prev = _dict[i]
    return res


if  __name__ == "__main":
    roman = input().strip()
    print(roman_to_int(roman))
    